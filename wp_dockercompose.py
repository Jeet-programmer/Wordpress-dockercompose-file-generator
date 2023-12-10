# Define the string you want to write to the file
import shutil

# Wordpress_dockerfile_name=input("Enter Dockerfile name remember it will contain a _wp suffix by default: ")
# wordpress_web_port=input("Enter a port for your Wordpress: ")
# wordpress_db_port=input("Enter a port for your Wordpress Database: ")


def wp_docker_compose(Wordpress_dockerfile_name,wordpress_web_port,wordpress_db_port):
    my_string = f'''name: {Wordpress_dockerfile_name}_wp
services:
  app:
    cpu_shares: 90
    command: []
    depends_on:
      db:
        condition: service_started
        required: true
    deploy:
      resources:
        limits:
          memory: 5804M
    environment:
      - WORDPRESS_DB_HOST=db
      - WORDPRESS_DB_NAME=wordpress
      - WORDPRESS_DB_PASSWORD=casaos
      - WORDPRESS_DB_USER=casaos
    image: wordpress:latest
    labels:
      icon: https://cdn.jsdelivr.net/gh/walkxcode/dashboard-icons/png/wordpress.png
    ports:
      - mode: ingress
        target: 80
        published: "{wordpress_web_port}"
        protocol: tcp
    restart: unless-stopped
    volumes:
      - type: bind
        source: /DATA/AppData/{Wordpress_dockerfile_name}/html
        target: /var/www/html
        bind:
          create_host_path: true
    x-casaos:
      envs:
        - container: WORDPRESS_DB_HOST
          description:
            en_us: Database host
        - container: WORDPRESS_DB_USER
          description:
            en_us: Database user
        - container: WORDPRESS_DB_PASSWORD
          description:
            en_us: Database password
        - container: WORDPRESS_DB_NAME
          description:
            en_us: Database name
      ports:
        - container: "80"
          description:
            en_us: "Container Port: 80"
      volumes:
        - container: /var/www/html
          description:
            en_us: "Container Path: /var/www/html"
    devices: []
    cap_add: []
    networks:
      - default
    privileged: false
    container_name: ""
  db:
    cpu_shares: 90
    command: []
    deploy:
      resources:
        limits:
          memory: 5804M
    environment:
      - MYSQL_DATABASE=wordpress
      - MYSQL_PASSWORD=casaos
      - MYSQL_ROOT_PASSWORD=casaos
      - MYSQL_USER=casaos
    image: mysql:5.7
    labels:
      icon: https://cdn.jsdelivr.net/gh/walkxcode/dashboard-icons/png/wordpress.png
    restart: unless-stopped
    volumes:
      - type: bind
        source: /DATA/AppData/{Wordpress_dockerfile_name}/mysql
        target: /var/lib/mysql
        bind:
          create_host_path: true
    x-casaos:
      envs:
        - container: MYSQL_DATABASE
          description:
            en_us: Database name
        - container: MYSQL_USER
          description:
            en_us: Database user
        - container: MYSQL_PASSWORD
          description:
            en_us: Database password
        - container: MYSQL_ROOT_PASSWORD
          description:
            en_us: Database root password
      ports:
        - container: "{wordpress_db_port}"
          description:
            en_us: "Container Port: {wordpress_db_port}"
      volumes:
        - container: /var/lib/mysql
          description:
            en_us: "Container Path: /var/lib/mysql"
    ports: []
    devices: []
    cap_add: []
    networks:
      - default
    privileged: false
    container_name: ""
networks:
  default:
    name: {Wordpress_dockerfile_name}_default
x-casaos:
  architectures:
    - amd64
    - arm
  author: self
  category: self
  hostname: ""
  icon: https://cdn.jsdelivr.net/gh/walkxcode/dashboard-icons/png/wordpress.png
  index: /
  main: app
  port_map: "{wordpress_web_port}"
  scheme: http
  store_app_id: big-bear-wordpress
  tagline:
    en_us: WordPress
  thumbnail: ""
  title:
    custom: {Wordpress_dockerfile_name}
    en_us: WordPress
'''
# Specify the file path (change 'your_file.txt' to your desired file name)
    file_path = f'dockercompose.txt'

    # Open the file in write mode ('w' for write)
    # If the file does not exist, it will be created. If it exists, its content will be overwritten.
    with open(file_path, 'w') as file:
        # Write the string to the file
        file.write(my_string)

    # Print a message indicating that the operation was successful
    print(f'String has been written to {file_path}')


def convert_txt_to_yml(txt_file_path, yml_file_path):
    # Copy the text file to a new file with the .yml extension
    shutil.copyfile(txt_file_path, yml_file_path)

    print(f"Conversion complete. YAML file saved to {yml_file_path}")

# # Example usage:
# txt_file_path = f'{Wordpress_dockerfile_name}.txt'  # Change this to your text file path
# yaml_file_path = f'docker compose.yml'  # Change this to your desired YAML file path

# convert_txt_to_yml(txt_file_path, yaml_file_path)
