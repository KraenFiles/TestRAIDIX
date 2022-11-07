Name:		RAIDIX
Version:	1.0
Release:	1%{?dist}
Summary:	Development program output on display "Test task in RAIDIX!"
License:	License
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	g++

%description
Development program output on display "Test task in RAIDIX!"

%prep
rm -rf %{name}-%{version}
mkdir -p %{name}-%{version}
tar -xzvf %{SOURCE0} -C %{_builddir}/%{name}-%{version}

%build
cd %{name}-%{version}
make

%install
cd %{name}-%{version}
make install DESTDIR=%{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/*

%files
/%{name}
