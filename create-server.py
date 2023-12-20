#Creating a server on digital ocean

import digitalocean

name = input("Please enter a name for your droplet: ")
do_token = "dop_v1_0a5e40c6ae1674e7c35d89e2a5fdc1597602d0a3836d5e5f4fd7407bd0dd6fed"
password = input("Please create a password for your server: ") 

droplet = digitalocean.Droplet(token=do_token,
    name= name,
    region="nyc1",
    image= "ubuntu-20-04-x64",
    size_slug= "s-1vcpu-1gb", # 1GB RAM
    ssh_password= password,
    backups=True)

if __name__ == "__main__":
    droplet.create()



#Listing all droplets
    
manager = digitalocean.Manager(token=do_token)
print(manager.get_all_droplets())