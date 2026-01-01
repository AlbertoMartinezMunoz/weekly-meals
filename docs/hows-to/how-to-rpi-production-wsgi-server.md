# How to Deploy a Production WSGI Server in a RPi

## RPi Setup

First the RPi existing packages should be updated:

```sh
sudo apt update
sudo apt upgrade -y
```

After that, to begin building your Python web server, we need to install Apache, the WSGI module (which allows Apache to communicate with Python applications), and Python's virtual environment package:

```sh
sudo apt install apache2 libapache2-mod-wsgi-py3 python3-venv
```

## Project Setup

Go to the Apache's default document root usually `/var/www` and clone the git project

```sh
sudo mkdir /var/www/weekly-meals
cd /var/www/weekly-meals
```

Then, change ownership of the directory to your user (e.g., pi) and clone the repo inside:

```sh
sudo chown pi:pi /var/www/weekly-meals
git clone https://github.com/AlbertoMartinezMunoz/weekly-meals.git .
```

After that, activate the virtual environment and install all the dependences:

```sh
# Set up a virtual environment
python3 -m venv .venv

# Activate it
. .venv/bin/activate

# Install dependencies
pip install -r requirements.txt --upgrade
```

Make a note of your site packages path you will need this in step 6 below you can do this by typing:

```sh
python3 -c "import site; print(site.getsitepackages())"
```

The output you are looking for should look something like this:

```
/var/www/myflaskapp/venv/lib/python3.11/site-packages
```

After finishing installing dependencies or packages, we can deactivate the virtual environment:

```sh
deactivate
```

## Apache Setup

Create an Apache configuration file `sudo nano /etc/apache2/sites-available/weekly-meals.conf` with the following contents (replace your_raspberrypi_ip_or_domain with your IP address for now):

```apacheconf
<VirtualHost *:80>
    ServerName your_raspberrypi_ip_or_domain
    WSGIDaemonProcess weekly-meals python-home=/var/www/weekly-meals/.venv python-path=/var/www/weekly-meals:/var/www/weekly-meals/src
    WSGIProcessGroup weekly-meals
    WSGIScriptAlias / /var/www/weekly-meals/weekly-meals.wsgi

    <Directory /var/www/weekly-meals>
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

After that, enable your new site and disable the default site:

```sh
sudo a2ensite weekly-meals.conf
sudo a2dissite 000-default.conf
```

Then, change the ownership of the application directory to www-data:

```sh
sudo chown -R www-data:www-data /var/www/weekly-meals
```

And set correct file and directory permissions:

```sh
sudo find /var/www/weekly-meals -type d -exec chmod 755 {} \;
sudo find /var/www/weekly-meals -type f -exec chmod 644 {} \;
```

Restart Apache to apply the changes:

```sh
sudo systemctl restart apache2
```

## Firewall Setup

```sh
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A OUTPUT -p tcp --sport 80 -j ACCEPT
```

The rules should be saved from the root account, as root use the `iptables-save` command to save the rules in the file `/etc/iptables/rules.v4`

```shell
sudo -i
sudo iptables-save > /etc/iptables/rules.v4
```

## References

[Build a Python Web Server on Raspberry Pi: Secure HTTPS with Flask](https://websonic.co.uk/blog/build-a-python-web-server-on-raspberry-pi-secure-https-with-flask)