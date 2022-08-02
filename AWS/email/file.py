# -*- coding: utf-8 -*-
import boto3

#Cria um serviço com as ordens das minhas credenciais da AWS
ses = boto3.client(
    service_name = 'ses',
    region_name = 'us-east-1',
    aws_access_key_id = '...',
    aws_secret_access_key = '...'
)

#Corpo que envia o email através do serviço SES da AWS
ses.send_email(
    Destination={
        'ToAddresses': ['email@gmail.com',], #Email de quem vai receber
    },

    Message ={
        'Body': {
            'Text': {
                'Charset': 'utf-8',
                'Data': "teste", #Texto do email
            },
        },
        'Subject':{
                'Charset': 'utf-8',
                'Data': "titulo", #Titulo do email

        },
    },
    Source='email@gmail.com' #Email que vai enviar
)