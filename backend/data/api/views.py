
from datetime import date
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
import csv
import pandas as pd

from data.models import Data
from .serializers import DataSerializer

class DataViewSet(ModelViewSet):
    # queryset = Data.objects.all().order_by('-id')
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    
    @action(detail=False, methods=["POST"])
    def upload_csv(self, request):
        file = request.FILES.get("file")
        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        if not file.name.endswith(".csv"):
            return Response({"error": "File must be a CSV"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Read CSV file into pandas DataFrame
            df = pd.read_csv(file)
            df.columns = df.columns.str.lower()

            # Debug statement to print out adjusted column names
            print("Adjusted column names:", df.columns)
            
            # Infer and convert data types
            for col in df.columns:
                
                if col == 'score':
                    # Replace 'Not Available' with a default value
                    df[col] = df[col].replace('Not Available', 0)
                    # Replace empty values with 0
                    df[col] = df[col].fillna(0)

                df_converted = pd.to_numeric(df[col], errors='coerce')
                if not df_converted.isna().all():
                    df[col] = df_converted
                    continue
                try:
                    df[col] = pd.to_datetime(df[col], format='%d/%m/%Y')
                    continue
                except (ValueError, TypeError):
                    pass
                if len(df[col].unique()) / len(df[col]) < 0.5:
                    df[col] = pd.Categorical(df[col])

            # Save DataFrame to database
            instances = []
            for row in df.to_dict(orient="records"):
                instance = Data(
                    name=row['name'],
                    birthdate=row['birthdate'],
                    score=row['score'],
                    grade=row['grade']
                )
                instances.append(instance)
            Data.objects.bulk_create(instances)

            return Response({"success": "File uploaded successfully"}, status=status.HTTP_200_OK)

        
        
        except Exception as e:
            print("Error processing CSV file:", e)  # Debug statement
            return Response({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
