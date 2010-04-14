Summary:	LSI Logic MegaRAID Linux MegaCLI utility
Summary(pl.UTF-8):	Linuksowe narzędzie MegaCLI dla macierzy LSI Logic MegaRAID
Name:		megacli-sas
Version:	1.01.39
Release:	2
License:	LSI
Group:		Base
Source0:	http://www.lsi.com/support/downloads/megaraid/miscellaneous/linux/%{version}_Linux_Cli.zip
# Source0-md5:	89dc235b90392eef0893ef461ce06500
URL:		http://www.lsi.com/storage_home/products_home/internal_raid/megaraid_sas/megaraid_sas_8480e/#Miscellaneous
BuildRequires:	rpm-utils
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin

# no debug symbols
%define		_enable_debug_packages	0

%description
Tool to control MegaRAID controllers:
- MegaRAID SAS 84016E
- MegaRAID SAS 8408E
- MegaRAID SAS 8480E
- MegaRAID SAS 8308ELP
- MegaRAID SAS 8344ELP
- MegaRAID SAS 8304ELP
- MegaRAID SAS 8300XLP
- MegaRAID SAS 8708EM2
- MegaRAID SAS 8880EM2

%description -l pl.UTF-8
Narzędzie do sterowania kontrolerami MegaRAID:
- MegaRAID SAS 84016E
- MegaRAID SAS 8408E
- MegaRAID SAS 8480E
- MegaRAID SAS 8308ELP
- MegaRAID SAS 8344ELP
- MegaRAID SAS 8304ELP
- MegaRAID SAS 8300XLP
- MegaRAID SAS 8708EM2
- MegaRAID SAS 8880EM2

%prep
%setup -qc
rpm2cpio *.rpm | cpio -i -d

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
