from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    if request.method == "POST":
        in1 = request.POST.get('inputone')
        in2 = request.POST.get('inputsecond')
        # print(in1)
        # print(in2)
        if request.POST.get('sub1'):
             if in1 and in2 :
                output = int(in1 ) + int(in2)
                # print(output)
             else:
                 output = "please Enter valid Input"
        elif request.POST.get('sub2'):
              if in1 and in2 :
                output = int(in1 ) - int(in2)
                # print(output)
              else:
                 output = "please Enter valid Input"
        elif request.POST.get('sub3'):
             if in1 and in2 :
                output = int(in1 ) * int(in2)
                # print(output)
             else:
                 output = "please Enter valid Input"
        elif request.POST.get('sub4'):
            if in1 and in2 :
                output = int(in1 ) / int(in2)
                # print(output)
            else:
                 output = "please Enter valid Input"
        elif request.POST.get('sub5'):
             if in1 and in2 :
                output = int(in1 ) % int(in2)
                # print(output)
             else:
                 output = "please Enter valid Input"
        context ={
        'output':output,
        'inp1':in1,
        'inp2':in2
              }
    else:
        output = "0"
        context ={
            'output':output,
            'inp1':"0",
            'inp2':"0",
        }
    return render(request,'index.html',context)
