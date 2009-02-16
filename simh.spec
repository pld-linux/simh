#
Summary:	The Computer History Simulation Project
Summary(pl.UTF-8):	Symulator historycznych komputerów
Name:		simh
Version:	3.8.1
Release:	1
License:	Almost public domain (see sources for details)
Group:		Applications/Emulators
Source0:	http://simh.trailing-edge.com/sources/%{name}v38-1.zip
# Source0-md5:	e15f65a82e21ea49e14b438326d93d5c
Source1:	http://simh.trailing-edge.com/pdf/%{name}_doc.pdf
# Source1-md5:	65d8b407e903f240ac47e0310e599a9b
Source2:	http://simh.trailing-edge.com/pdf/%{name}_swre.pdf
# Source2-md5:	db147325aa69f8b9e709971774edc91b
Source3:	http://simh.trailing-edge.com/pdf/%{name}_faq.pdf
# Source3-md5:	cbb442ddc136f9b26d6917033fd03b18
Source4:	http://simh.trailing-edge.com/pdf/altairz80_doc.pdf
# Source4-md5:	224f1c3ec61c7fc989597a9e10241cb8
Source5:	http://simh.trailing-edge.com/pdf/nova_doc.pdf
# Source5-md5:	f4b79a472fb2628f9b4907c1ed0e7d17
Source6:	http://simh.trailing-edge.com/pdf/pdp1_doc.pdf
# Source6-md5:	01c59c15d5686559083e814568f21cd5
Source7:	http://simh.trailing-edge.com/pdf/pdp18b_doc.pdf
# Source7-md5:	ef9dba09c796d88df5b99112d01d7805
Source8:	http://simh.trailing-edge.com/pdf/pdp8_doc.pdf
# Source8-md5:	04ab4961c3420e9d4dd4ca58f3593a1f
Source9:	http://simh.trailing-edge.com/pdf/pdp10_doc.pdf
# Source9-md5:	fef263eb13c215e5fa0826d56bc5aa2b
Source10:	http://simh.trailing-edge.com/pdf/pdp11_doc.pdf
# Source10-md5:	e3cb433af64e5d8cb398333410736a49
Source11:	http://simh.trailing-edge.com/pdf/vax780_doc.pdf
# Source11-md5:	b137fdc66a92587ba9b8e13a7ecf0297
Source12:	http://simh.trailing-edge.com/pdf/vax_doc.pdf
# Source12-md5:	39548e29c41cea1469c4d82c9209ab16
Source13:	http://simh.trailing-edge.com/pdf/gri_doc.pdf
# Source13-md5:	fc46ce0864e8a655e85c1d007a2786fe
Source14:	http://simh.trailing-edge.com/pdf/i1401_doc.pdf
# Source14-md5:	89f1d7888096c5e28bb97b876f66942d
Source15:	http://simh.trailing-edge.com/pdf/i1620_doc.pdf
# Source15-md5:	75f7ad65dc2c4ce1dff0e31674425603
Source16:	http://simh.trailing-edge.com/pdf/i7094_doc.pdf
# Source16-md5:	4524712d7d3c013a9a4db0f3db1bdcce
Source17:	http://simh.trailing-edge.com/pdf/id_doc.pdf
# Source17-md5:	4a7960b00544bc49c0fa7d62b4b6ba9b
Source18:	http://simh.trailing-edge.com/pdf/hp2100_doc.pdf
# Source18-md5:	3cdb2da2e8d36168032cb0a93b8ff837
Source19:	http://simh.trailing-edge.com/pdf/h316_doc.pdf
# Source19-md5:	2a61c714d68503b4df3b31998830088d
Source20:	http://simh.trailing-edge.com/pdf/lgp_doc.pdf
# Source20-md5:	f7d20390533e6817097779ffb9914d60
Source21:	http://simh.trailing-edge.com/pdf/sds_doc.pdf
# Source21-md5:	61a2769bd39625774abb2991bc90d08c

URL:		http://simh.trailing-edge.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Computer History Simulation Project is a loose Internet-based
collective of people interested in restoring historically significant
computer hardware and software systems by simulation. The goal of the
project is to create highly portable system simulators and to publish
them as freeware on the Internet, with freely available copies of
significant or representative software.

Currently simh can emulate following ancient computers: altair
altairz80 eclipse gri h316 hp2100 i1401 i1620 i7094 ibm1130 id16 id32
lgp nova pdp1 pdp10 pdp11 pdp15 pdp4 pdp7 pdp8 pdp9 s3 sds vax vax780.


%description -l pl.UTF-8
Celem projektu simh jest utrwalenie pamięci o historycznym sprzęcie
komputerowym i oprogramowaniu poprzez stworzenie przenośnego
symulatora sprzętu, który miał duże znaczenie dla rozwoju komputerów
oraz dostarczenie kopii zabytkowego oprogramowania.

Obecnie simh potrafi emulować nastepujące architektury: altair
altairz80 eclipse gri h316 hp2100 i1401 i1620 i7094 ibm1130 id16 id32
lgp nova pdp1 pdp10 pdp11 pdp15 pdp4 pdp7 pdp8 pdp9 s3 sds vax vax780.

%package doc
Summary:	simh documentation
Summary(pl.UTF-8):	Dokumentacja simh
Group:		Documentation

%description doc
The Computer History Simulation Project documentation.

%description doc -l pl.UTF-8
Dokumentacja pakietu simh. Zawiera ogólne informacje dotyczace
symulatorów oraz szczegółowy opis poszczególnych obsługiwanych
architektur.

%prep
%setup -c -q

mkdir BIN

%build

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_docdir}/%{name}-doc-%{version}}

install BIN/altair    $RPM_BUILD_ROOT%{_bindir}/simh-altair
install BIN/altairz80 $RPM_BUILD_ROOT%{_bindir}/simh-altairz80
install BIN/eclipse   $RPM_BUILD_ROOT%{_bindir}/simh-eclipse
install BIN/gri       $RPM_BUILD_ROOT%{_bindir}/simh-gri
install BIN/h316      $RPM_BUILD_ROOT%{_bindir}/simh-h316
install BIN/hp2100    $RPM_BUILD_ROOT%{_bindir}/simh-hp2100
install BIN/i1401     $RPM_BUILD_ROOT%{_bindir}/simh-i1401
install BIN/i1620     $RPM_BUILD_ROOT%{_bindir}/simh-i1620
install BIN/i7094     $RPM_BUILD_ROOT%{_bindir}/simh-i7094
install BIN/ibm1130   $RPM_BUILD_ROOT%{_bindir}/simh-ibm1130
install BIN/id16      $RPM_BUILD_ROOT%{_bindir}/simh-id16
install BIN/id32      $RPM_BUILD_ROOT%{_bindir}/simh-id32
install BIN/lgp       $RPM_BUILD_ROOT%{_bindir}/simh-lgp
install BIN/nova      $RPM_BUILD_ROOT%{_bindir}/simh-nova
install BIN/pdp1      $RPM_BUILD_ROOT%{_bindir}/simh-pdp1
install BIN/pdp10     $RPM_BUILD_ROOT%{_bindir}/simh-pdp10
install BIN/pdp11     $RPM_BUILD_ROOT%{_bindir}/simh-pdp11
install BIN/pdp15     $RPM_BUILD_ROOT%{_bindir}/simh-pdp15
install BIN/pdp4      $RPM_BUILD_ROOT%{_bindir}/simh-pdp4
install BIN/pdp7      $RPM_BUILD_ROOT%{_bindir}/simh-pdp7
install BIN/pdp8      $RPM_BUILD_ROOT%{_bindir}/simh-pdp8
install BIN/pdp9      $RPM_BUILD_ROOT%{_bindir}/simh-pdp9
install BIN/s3        $RPM_BUILD_ROOT%{_bindir}/simh-s3
install BIN/sds       $RPM_BUILD_ROOT%{_bindir}/simh-sds
install BIN/vax       $RPM_BUILD_ROOT%{_bindir}/simh-vax
install BIN/vax780    $RPM_BUILD_ROOT%{_bindir}/simh-vax780

install %{SOURCE1}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/simh_doc.pdf
install %{SOURCE2}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/simh_swre.pdf
install %{SOURCE3}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/simh_faq.pdf
install %{SOURCE4}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/altairz80_doc.pdf
install %{SOURCE5}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/nova_doc.pdf
install %{SOURCE6}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/pdp1_doc.pdf
install %{SOURCE7}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/pdp18b_doc.pdf
install %{SOURCE8}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/pdp8_doc.pdf
install %{SOURCE9}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/pdp10_doc.pdf
install %{SOURCE10}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/pdp11_doc.pdf
install %{SOURCE11}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/vax780_doc.pdf
install %{SOURCE12}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/vax_doc.pdf
install %{SOURCE13}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/gri_doc.pdf
install %{SOURCE14}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/i1401_doc.pdf
install %{SOURCE15}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/i1620_doc.pdf
install %{SOURCE16}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/i7094_doc.pdf
install %{SOURCE17}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/id_doc.pdf
install %{SOURCE18}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/hp2100_doc.pdf
install %{SOURCE19}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/h316_doc.pdf
install %{SOURCE20}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/lgp_doc.pdf
install %{SOURCE21}	$RPM_BUILD_ROOT%{_docdir}/%{name}-doc-%{version}/sds_doc.pdf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc 0readme_38.txt 0readme_ethernet.txt
%attr(755,root,root) %{_bindir}/simh-altair
%attr(755,root,root) %{_bindir}/simh-altairz80
%attr(755,root,root) %{_bindir}/simh-eclipse
%attr(755,root,root) %{_bindir}/simh-gri
%attr(755,root,root) %{_bindir}/simh-h316
%attr(755,root,root) %{_bindir}/simh-hp2100
%attr(755,root,root) %{_bindir}/simh-i1401
%attr(755,root,root) %{_bindir}/simh-i1620
%attr(755,root,root) %{_bindir}/simh-i7094
%attr(755,root,root) %{_bindir}/simh-ibm1130
%attr(755,root,root) %{_bindir}/simh-id16
%attr(755,root,root) %{_bindir}/simh-id32
%attr(755,root,root) %{_bindir}/simh-lgp
%attr(755,root,root) %{_bindir}/simh-nova
%attr(755,root,root) %{_bindir}/simh-pdp1
%attr(755,root,root) %{_bindir}/simh-pdp10
%attr(755,root,root) %{_bindir}/simh-pdp11
%attr(755,root,root) %{_bindir}/simh-pdp15
%attr(755,root,root) %{_bindir}/simh-pdp4
%attr(755,root,root) %{_bindir}/simh-pdp7
%attr(755,root,root) %{_bindir}/simh-pdp8
%attr(755,root,root) %{_bindir}/simh-pdp9
%attr(755,root,root) %{_bindir}/simh-s3
%attr(755,root,root) %{_bindir}/simh-sds
%attr(755,root,root) %{_bindir}/simh-vax
%attr(755,root,root) %{_bindir}/simh-vax780

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-doc-%{version}
