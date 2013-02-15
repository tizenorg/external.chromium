Name:       chromium
Summary:    chromium library
Version:    1.0
Release:    1
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  cmake

%description
chromium library

%package devel
Summary:    chromium library (devel)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
chromium library (devel)

%prep
%setup -q

%build
MAJORVER=`echo %{version} | awk 'BEGIN {FS="."}{print $1}'`
%ifarch %{ix86}
CXXFLAGS="$CXXFLAGS -D_OSP_DEBUG_ -D_OSP_X86_ -D_OSP_EMUL_" cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} -DFULLVER=%{version} -DMAJORVER=${MAJORVER}
%else
CXXFLAGS="$CXXFLAGS -D_OSP_DEBUG_ -D_OSP_ARMEL_" cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} -DFULLVER=%{version} -DMAJORVER=${MAJORVER}
%endif
# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{name}-%{version}/LICENSE  %{buildroot}/usr/share/license/%{name}

%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest chromium.manifest
%defattr(-,root,root,-)
/usr/share/license/%{name}
%{_libdir}/libchromium.so*

%files devel
%defattr(-,root,root,-)
%{_includedir}/chromium/*
%{_libdir}/pkgconfig/chromium.pc
