from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postdata = request.POST

        firstname = postdata.get('fname')
        lastname = postdata.get('lname')
        phone = postdata.get('num')
        email = postdata.get('mail')
        password = postdata.get('pass')
        # validation
        value = {
            'firstname': firstname,
            'lastname': lastname,
            'phone': phone,
            'email': email
        }
        error_msg = None

        customer = Customer(first_name=firstname,
                            last_name=lastname,
                            phone=phone,
                            email=email,
                            password=password)
        error_msg = self.validateCustomer(customer)

        ##saving
        if not error_msg:
            print(firstname, lastname, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_msg,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self ,customer):
        error_msg = None
        if not customer.first_name:
            error_msg = 'first name is required !'
        elif len(customer.first_name) < 3:
            error_msg = 'first name should be more then 3 character'
        elif not customer.last_name:
            error_msg = 'last name is required !'
        elif len(customer.last_name) < 3:
            error_msg = 'last name should be more then 3 character'
        elif not customer.phone:
            error_msg = 'phone number is required !'
        elif len(customer.phone) < 10:
            error_msg = 'phone number should be more then 10 character'
        elif not customer.email:
            error_msg = 'email is required !'
        elif not customer.password:
            error_msg = 'password is required !'
        elif len(customer.password) < 5:
            error_msg = 'password should be more then 5 character'
        elif customer.isExist():
            error_msg = 'Email address allready register'

        return error_msg