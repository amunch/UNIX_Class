#!/bin/sh

export PATH=/afs/nd.edu/user15/pbui/pub/anaconda-2.3.0/bin:$PATH

if [ $# != 1 ]; then
    echo "usage: $0 path"
    exit 1
fi

if ! command -v markdown_py > /dev/null; then
    echo "error: you need to install markdown_py!"
    exit 2
fi


if ! command -v elinks > /dev/null; then
    echo "error: you need to install elinks!"
    exit 3
fi

stylize() {
     sed -e 's|pre>|p style="color:green;">|g' \
	 -e 's|<h\([0-9]\)>|<h\1 style="color:yellow;">|g' \
	 -e 's|<strong>|<strong style="color:magenta;">|g'
}


ELINKS_FLAGS="-force-html -dump -dump-width $(tput cols) -no-numbering -no-references"

case $(elinks -version | awk '{print $2}' | head -n 1) in
    0.12*|0.13*)
    ELINKS_FLAGS="$ELINKS_FLAGS -dump-color-mode 1"
    ;;
esac

exec markdown_py $@ |
     stylize |
     elinks ${ELINKS_FLAGS} |
     less -Rcgm
