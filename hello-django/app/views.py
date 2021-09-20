from django.http.response import HttpResponse
from django.http.request import HttpRequest

def hello_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World!")

def hey_name(request: HttpRequest, name) -> HttpResponse:
    return HttpResponse(f"Hey, {name}!")

def birthday(request: HttpRequest, end, birthyear) -> HttpResponse:
    age = end - birthyear
    return HttpResponse(f"You will be {age} in {end}!")

def burber(request: HttpRequest, burgers, fries, drinks) -> HttpRequest:
    burger_total = 4.5*burgers
    fries_total = 1.5*fries
    total = burger_total + fries_total + drinks
    return HttpResponse(f"You ordered {burgers} burgers, {fries} fries, and {drinks} drinks. Your total is ${total}!")

def near_hundred(request: HttpRequest, n) -> HttpResponse:
  if n >= 90 and n <= 110:
    return HttpResponse(True)
  elif n >= 190 and n <= 210:
    return HttpResponse(True)
  else:
    return HttpResponse(False)

def string_splosion(request: HttpRequest, str) -> HttpResponse:
  new = ""
  for i in range(len(str)):
    new += str[:i +1]
  return HttpResponse(new)

def cat_dog(request: HttpRequest, str) -> HttpResponse:
  cat = 0
  dog = 0
  for i in range(len(str)):
    if str[i:i+3] == "cat":
      cat += 1
    elif str[i:i+3] == "dog":
      dog += 1
  if cat == dog:
    return HttpResponse(True)
  else:
    return HttpResponse(False)

def lone_sum(request: HttpRequest, a, b, c) -> HttpResponse:
    if a == b == c:
        return HttpResponse(0)
    elif b == c:
        return HttpResponse(a)
    elif a == c:
        return HttpResponse(b)
    elif a == b:
        return HttpResponse(c)
    else:
        return HttpResponse(a + b + c)
  