FROM python:3.11-slim

ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . .

ENV VIRTUAL_ENV=/app/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install .
RUN mkdir $APP_HOME/user_data
RUN cd $APP_HOME/user_data

WORKDIR $APP_HOME/user_data

ENTRYPOINT [ "a_book" ]
