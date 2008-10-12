#
Summary:	The Computer History Simulation Project
Summary(pl.UTF-8):	Symulator historycznych komputerów
Name:		simh
Version:	3.8.0
Release:	0.1
License:	Almost public domain (see sources for details)
Group:		Applications/Emulators
Source0:	http://simh.trailing-edge.com/sources/%{name}v38-0.zip
# Source0-md5:	d4bf6b7708e1f429e1e9b3c9e3e93b24
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

%prep
%setup -c -q

mkdir BIN

%build

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

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
