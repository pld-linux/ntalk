Summary:	Talk client for one-on-one Internet chatting.
Summary(de):	Talk-client f�r 1:1-Internet-Schw�tzchen.
Summary(fr):	Client talk pour les conversations � deux sur l'Internet.
Summary(pl):	Klient talk do rozm�w jeden-na-jeden w Internecie.
Summary(tr):	Internet �zerinde birebir konu�ma - talk - sistemi.
Name:		ntalk
Version:	0.11
Release:	1
Copyright:	BSD
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source:		ftp://sunsite.unc.edu/pub/Linux/system/network/chat/netkit-ntalk-%{version}.tar.gz
Patch0:		netkit-ntalk-misc.patch
Patch1:		netkit-ntalk-install.patch
Patch2:		netkit-ntalk-otalk.patch
Requires:	inetd
BuildRequires:	ncurses-devel
Obsoletes:	talk
Buildroot:	/tmp/%{name}-%{version}-root

%description
This package provides a daemon for the Internet talk protocol,
which allows one-on-one chatting between users on different systems.

%description -l de
Dieses Paket enth�lt einen D�mon f�r das Internet-Talk-
Protokoll, das das Chatten von zwei Benutzern auf verschiedenen
Systemen erm�glicht.

%description -l fr
Ce package offre un d�mon pour le 'Internet Talk Protocol',
qui permet la conversation un-a-un dans la discussion entre les
utilisateurs de diff�rents syst�mes.

%description -l pl
Pakiet ten zawiera demona dla internetowego protoko�u talk, 
kt�ry umo�liwia	komunikacj� mi�dzy u�ytkownikami na r�nych systemach.

%description -l tr
Bu paket internet talk hizmeti i�in bir istemci ve sunucu i�ermektedir. Bu
program 'konu�mak' isteyen ki�ilerin terminalinde iki b�l�m a�acakt�r.
Kullan�c�lardan her biri kendi yazd�klar�n� ekran�n alt k�sm�nda, kar��
taraf�n yazd�klar�n� ise �st k�s�mda g�receklerdir.

%package client
Summary:        Talk client for one-on-one Internet chatting.
Summary(de):    Talk-client f�r 1:1-Internet-Schw�tzchen.
Summary(fr):    Client talk pour les conversations � deux sur l'Internet.
Summary(pl):    Klient talk do rozm�w jeden-na-jeden w Internecie.
Summary(tr):    Internet �zerinde birebir konu�ma - talk - sistemi.
Group:          Applications/Networking
Group(pl):      Aplikacje/Sieciowe
Requires:	%{name} = %{version}

%description client
This package provides a client for the Internet talk protocol,
which allows one-on-one chatting between users on different systems.

%description -l de client
Dieses Paket enth�lt einen Client f�r das Internet-Talk-
Protokoll, das das Chatten von zwei Benutzern auf verschiedenen
Systemen erm�glicht.

%description -l fr client
Ce package offre un client pour le 'Internet Talk Protocol',
qui permet la conversation un-a-un dans la discussion entre les
utilisateurs de diff�rents syst�mes.

%description -l pl client
Pakiet ten zawiera klienta dla internetowego protoko�u talk,
kt�ry umo�liwia komunikacj� mi�dzy u�ytkownikami na r�nych systemach.

%description -l tr client
Bu paket internet talk hizmeti i�in bir istemci ve sunucu i�ermektedir. Bu
program 'konu�mak' isteyen ki�ilerin terminalinde iki b�l�m a�acakt�r.
Kullan�c�lardan her biri kendi yazd�klar�n� ekran�n alt k�sm�nda, kar��
taraf�n yazd�klar�n� ise �st k�s�mda g�receklerdir.

%prep
%setup -q -n netkit-ntalk-0.11
%patch0 -p1
%patch1 -p1
export POSIXLY_CORRECT=1
%patch2 -p0
unset POSIXLY_CORRECT

%build

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS -w -I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,8}}

make install INSTALLROOT=$RPM_BUILD_ROOT MANDIR=%{_mandir}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[18]/* \
	README BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz BUGS.gz

%attr(711,root,root) %{_sbindir}/*
%{_mandir}/man8/*

%files client
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/talk
%{_mandir}/man1/talk.1.gz
