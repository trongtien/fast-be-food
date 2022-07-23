FROM postgres:14.3
RUN localedef -i de_DE -c -f UTF-8 -A /usr/share/locale/locale.alias de_DE.UTF-8
ENV LANG de_DE.utf8

# USER postgres

# RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/14/main/pg_hba.conf

# RUN echo "listen_addresses='*'" >> /etc/postgresql/14/main/postgresql.conf

# EXPOSE 5432

# VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# CMD ["/usr/lib/postgresql/14/bin/postgres", "-D", "/var/lib/postgresql/14/main", "-c", "config_file=/etc/postgresql/14/main/postgresql.conf"]