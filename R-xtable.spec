#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-xtable
Version  : 1.8.4
Release  : 46
URL      : https://cran.r-project.org/src/contrib/xtable_1.8-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/xtable_1.8-4.tar.gz
Summary  : Export Tables to LaTeX or HTML
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : R-zoo
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n xtable
cd %{_builddir}/xtable

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641151044

%install
export SOURCE_DATE_EPOCH=1641151044
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xtable
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xtable
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library xtable
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc xtable || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/xtable/DESCRIPTION
/usr/lib64/R/library/xtable/INDEX
/usr/lib64/R/library/xtable/Meta/Rd.rds
/usr/lib64/R/library/xtable/Meta/data.rds
/usr/lib64/R/library/xtable/Meta/features.rds
/usr/lib64/R/library/xtable/Meta/hsearch.rds
/usr/lib64/R/library/xtable/Meta/links.rds
/usr/lib64/R/library/xtable/Meta/nsInfo.rds
/usr/lib64/R/library/xtable/Meta/package.rds
/usr/lib64/R/library/xtable/Meta/vignette.rds
/usr/lib64/R/library/xtable/NAMESPACE
/usr/lib64/R/library/xtable/NEWS
/usr/lib64/R/library/xtable/R/xtable
/usr/lib64/R/library/xtable/R/xtable.rdb
/usr/lib64/R/library/xtable/R/xtable.rdx
/usr/lib64/R/library/xtable/data/tli.txt.gz
/usr/lib64/R/library/xtable/doc/OtherPackagesGallery.R
/usr/lib64/R/library/xtable/doc/OtherPackagesGallery.Rnw
/usr/lib64/R/library/xtable/doc/OtherPackagesGallery.pdf
/usr/lib64/R/library/xtable/doc/index.html
/usr/lib64/R/library/xtable/doc/listOfTablesGallery.R
/usr/lib64/R/library/xtable/doc/listOfTablesGallery.Rnw
/usr/lib64/R/library/xtable/doc/listOfTablesGallery.pdf
/usr/lib64/R/library/xtable/doc/margintable.R
/usr/lib64/R/library/xtable/doc/margintable.Rnw
/usr/lib64/R/library/xtable/doc/margintable.pdf
/usr/lib64/R/library/xtable/doc/xtableGallery.R
/usr/lib64/R/library/xtable/doc/xtableGallery.Rnw
/usr/lib64/R/library/xtable/doc/xtableGallery.pdf
/usr/lib64/R/library/xtable/help/AnIndex
/usr/lib64/R/library/xtable/help/aliases.rds
/usr/lib64/R/library/xtable/help/paths.rds
/usr/lib64/R/library/xtable/help/xtable.rdb
/usr/lib64/R/library/xtable/help/xtable.rdx
/usr/lib64/R/library/xtable/html/00Index.html
/usr/lib64/R/library/xtable/html/R.css
/usr/lib64/R/library/xtable/tests/test.margintable.R
/usr/lib64/R/library/xtable/tests/test.matharray.R
/usr/lib64/R/library/xtable/tests/test.xalign.xdigits.xdisplay.R
/usr/lib64/R/library/xtable/tests/test.xtable.R
/usr/lib64/R/library/xtable/tests/test.xtable.data.frame.R
/usr/lib64/R/library/xtable/tests/test.xtable.xtableFtable.R
