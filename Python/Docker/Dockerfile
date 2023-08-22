FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y
RUN apt install git -y
RUN apt install python3-numpy -y 
RUN apt-get install python3-scipy -y
RUN apt-get install python3-netcdf4 -y

WORKDIR /usr/app/src/

RUN git clone https://github.com/queirozime/python_env_perfomance_test.git

WORKDIR /usr/app/src/python_env_perfomance_test

CMD ["bash", "python_job_script_docker"]