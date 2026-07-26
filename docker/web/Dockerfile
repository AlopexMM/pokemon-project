FROM node:20-alpine

ENV NODE_ENV=production

ENV PORT=3000

ENV HOSTNAME=0.0.0.0

RUN apk add --no-cache libc6-compat

WORKDIR /app

COPY apps/web/* ./

RUN corepack enable 

RUN echo $PWD

RUN pnpm install --frozen-lockfile && pnpm build

COPY ./.next/standalone ./

USER node

EXPOSE 3000

CMD ["node", "server.js"]
