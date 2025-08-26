# Use the lightweight official Nginx image
FROM nginx:alpine

# Copy your entire Portfolio folder content into nginx’s html directory
COPY ./Portfolio /usr/share/nginx/html

# Expose port 80 for the container
EXPOSE 80
