FROM yidigun/centos5

RUN set -ex \
        && yum update -y \
        && yum install -y \
                gcc \
                gcc-c++ \
                make

ADD https://www.python.org/ftp/python/2.1.3/Python-2.1.3.tgz /

RUN set -ex \
	&& tar xzvf Python-2.1.3.tgz \
	&& cd /Python-2.1.3 \
	&& ./configure --prefix /python \
	&& make -j4 \
	&& make install

FROM yidigun/centos5

COPY --from=0 /python /python

ENV PATH="/python/bin:${PATH}"
CMD ["/python/bin/python"]
