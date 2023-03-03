FROM node:16.18

ENV PORT=3000

COPY . /frontend-react-js
WORKDIR /frontend-react-js
RUN npm install
RUN chmod +x cmd_script.sh
EXPOSE ${PORT}
#CMD ["npm", "start"]
CMD /bin/bash ./cmd_script.sh
