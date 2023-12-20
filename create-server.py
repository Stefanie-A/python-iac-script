#Creating a droplet on digital ocean

import digitalocean

name = input("Please enter a name for your droplet: ")
do_token = ""
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