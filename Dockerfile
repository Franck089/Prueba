
FROM cervecera
LABEL maintainer="damaris.zavala@erona.io"

WORKDIR /schela

COPY docker/entrypoint.sh entrypoint.sh

#Un RUN corre un comando y crea una nueva capa sobre la imagen
RUN ["chmod", "+x", "entrypoint.sh"]

# entrypoint siempre se corre al correr la imagen
ENTRYPOINT ["sh", "entrypoint.sh"]

COPY /schela/. .
