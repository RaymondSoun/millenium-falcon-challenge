# start by pulling the python image
FROM python:3.10-bullseye AS builder

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install poetry

COPY . .

RUN poetry build -f wheel

FROM python:3.10-bullseye
WORKDIR /data
COPY --from=builder /app/dist/mfc-0.1.0-py3-none-any.whl ./
COPY ./data .
RUN pip install ./mfc-0.1.0-py3-none-any.whl && rm ./mfc-0.1.0-py3-none-any.whl

CMD [ "mfc", "serve", "./millennium-falcon.json"]