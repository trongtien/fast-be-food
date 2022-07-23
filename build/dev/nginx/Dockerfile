
FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY ./build/dev/nginx/nginx.conf /etc/nginx/conf.d

# RUN rm /etc/nginx/conf.d/default.conf
# RUN mkdir -p /etc/nginx/conf.d/

# COPY nginx.conf /etc/nginx/conf.d/default.conf

# CMD ["nginx", "-g", "daemon off;"]