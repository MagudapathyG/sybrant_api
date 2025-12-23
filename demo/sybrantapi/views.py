
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import PersonalProfile
from .serializers import PersonalProfileSerializer
from rest_framework import status


class ProfileFilterView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get filter parameters
        profile_id = request.GET.get('id', None)
        designation = request.GET.get('designation', None)
        department = request.GET.get('department', None)

        # Start with all profiles
        queryset = PersonalProfile.objects.all()
        
        # Apply filters
        if profile_id:
            queryset = queryset.filter(id=profile_id)
        if designation:
            queryset = queryset.filter(designation__icontains=designation)
        if department:
            queryset = queryset.filter(department__icontains=department)

        total_count = queryset.count()

        # Pagination
        try:
            limit = int(request.GET.get('limit', 10))
            offset = int(request.GET.get('offset', 0))
        except ValueError:
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "limit and offset must be integers"
            }, status=status.HTTP_400_BAD_REQUEST)

        queryset = queryset[offset:offset + limit]

        # Serialize data
        serializer = PersonalProfileSerializer(queryset, many=True)

        return Response({
            "status": status.HTTP_200_OK,
            "total": total_count,
            "limit": limit,
            "offset": offset,
            "data": serializer.data
        }, status=status.HTTP_200_OK)
