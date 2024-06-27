FROM node:18

WORkDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build