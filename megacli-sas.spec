Summary:	LSI Logic MegaRAID Linux MegaCLI utility
Summary(pl.UTF-8):	Linuksowe narzędzie MegaCLI dla macierzy LSI Logic MegaRAID
Name:		megacli-sas
Version:	8.00.40
Release:	1
License:	LSI
Group:		Base
# http://www.lsi.com/storage_home/products_home/internal_raid/megaraid_sas/6gb_s_value_line/sas9260-8i/
Source0:	MegaCli-8.00.40-1.i386.rpm
# Source0-md5:	c1d375ea9047bae259819ec0487d8398
BuildRequires:	rpm-utils
BuildRequires:	unzip
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin

# no debug symbols
%define		_enable_debug_packages	0

%description
Tool to control MegaRAID controllers:
- MegaRAID SAS 9240-4i
- MegaRAID SAS 9240-8i
- MegaRAID SAS 9260-4i
- MegaRAID SAS 9260-8i
- MegaRAID SAS 9260DE-8i
- MegaRAID SAS 9261-8i
- MegaRAID SAS 9280-4i4e
- MegaRAID SAS 9280-8e
- MegaRAID SAS 9280DE-8e
- MegaRAID SAS 9280-24i4e
- MegaRAID SAS 9280-16i4e
- MegaRAID SAS 9260-16i
- MegaRAID SAS 8704ELP
- MegaRAID SAS 8704EM2
- MegaRAID SAS 8708ELP
- MegaRAID SAS 8708EM2
- MegaRAID SAS 8880EM2
- MegaRAID SAS 8888ELP

%description -l pl.UTF-8
Narzędzie do sterowania kontrolerami MegaRAID:
- MegaRAID SAS 9240-4i
- MegaRAID SAS 9240-8i
- MegaRAID SAS 9260-4i
- MegaRAID SAS 9260-8i
- MegaRAID SAS 9260DE-8i
- MegaRAID SAS 9261-8i
- MegaRAID SAS 9280-4i4e
- MegaRAID SAS 9280-8e
- MegaRAID SAS 9280DE-8e
- MegaRAID SAS 9280-24i4e
- MegaRAID SAS 9280-16i4e
- MegaRAID SAS 9260-16i
- MegaRAID SAS 8704ELP
- MegaRAID SAS 8704EM2
- MegaRAID SAS 8708ELP
- MegaRAID SAS 8708EM2
- MegaRAID SAS 8880EM2
- MegaRAID SAS 8888ELP

%prep
%setup -qcT
rpm2cpio %{SOURCE0} | cpio -i -d

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
%ifarch %{ix86}
install -p opt/MegaRAID/MegaCli/MegaCli $RPM_BUILD_ROOT%{_sbindir}/MegaCli
%endif
%ifarch %{x8664}
install -p opt/MegaRAID/MegaCli/MegaCli64 $RPM_BUILD_ROOT%{_sbindir}/MegaCli
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/MegaCli
