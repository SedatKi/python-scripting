partition = input('Enter the partition: ')
service = input('Enter the service: ')
region = input('Enter the region: ')
account_id = int(input('Enter the account-id: '))
resource_id = int(input('Enter the resource-id: '))

print('The ARN format for your account is ' "arn", partition, service, region, account_id, resource_id, sep=":")
