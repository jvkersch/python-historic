FROM yidigun/centos5

RUN set -ex \
        && yum update -y \
        && yum install -y \
                gcc \
                gcc-c++ \
                make
RUN yum install -y patch

ADD https://legacy.python.org/download/releases/src/python1.1.tar.gz /python.tgz

COPY lcrypt.patch /

RUN set -ex \
	&& mkdir -p /python \
	&& tar xzvf python.tgz \
	&& cd /python-1.1 \
	&& patch -p1 < /lcrypt.patch \
	&& ./configure --prefix /python \
	&& make \
	&& mkdir -p /python/bin \
	&& make install

FROM yidigun/centos5

COPY --from=0 /python /python

ENV PATH="/python/bin:${PATH}"
CMD ["/python/bin/python"]
