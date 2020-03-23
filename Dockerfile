# Installation
FROM node:lts
#defined work dir
WORKDIR /home
#copy package to workdir
COPY ./package.json .
#install
RUN npm install --production
#port in machine
#EXPOSE 3000
#copy index.js and 
COPY . .
#run service with enterpoint
CMD [ "node", "helloworld.js" ]
