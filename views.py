from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import json
import timeit

@api_view(["POST"])
def fib_series(num):
	a=1
	b=1
	try:
		start_time=timeit.timeit()
		n=json.loads(num.body)
		if n == 1:
			b=1
		else:
			for i in range(2,n):
				temp=a+b
				a=b
				b=temp
		end_time=timeit.timeit()
		total_time=end_time-start_time
		return Response({'Nth term':b, 'Execution time':total_time})

	except Exception as e:
		return Response(e.args[0],status.HTTP_400_BAD_REQUEST)