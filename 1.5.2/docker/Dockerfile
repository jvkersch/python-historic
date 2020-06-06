FROM yidigun/centos5

RUN set -ex \
        && yum update -y \
        && yum install -y \
                gcc \
                gcc-c++ \
                make

ADD https://www.python.org/ftp/python/src/py152.tgz /python.tgz

RUN set -ex \
	&& mkdir -p /python \
	&& tar xzvf python.tgz \
	&& cd /Python-1.5.2 \
	&& ./configure --prefix /python \
	&& make \
	&& make install

FROM yidigun/centos5

COPY --from=0 /python /python

ENV PATH="/python/bin:${PATH}"
CMD ["/python/bin/python"]
