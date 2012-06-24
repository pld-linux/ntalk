Summary:	Talk client for one-on-one Internet chatting
Summary(de):	Talk-client f�r 1:1-Internet-Schw�tzchen
Summary(fr):	Client talk pour les conversations � deux sur l'Internet
Summary(pl):	Klient talk do rozm�w jeden-na-jeden w Internecie
Summary(tr):	Internet �zerinde birebir konu�ma - talk - sistemi
Name:		ntalk
Version:	0.17
Release:	2
License:	BSD
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.linux.org.uk/pub/linux/Networking/netkit/netkit-%{name}-%{version}.tar.gz
Source1:	%{name}d.inetd
Source2:	talkd.inetd
Patch0:		netkit-%{name}-misc.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	talk
Obsoletes:	ntalk-client

%description
This package provides a client for the Internet talk protocol, which
allows one-on-one chatting between users on different systems.

%description -l de
Dieses Paket enth�lt einen Client f�r das Internet-Talk- Protokoll,
das das Chatten von zwei Benutzern auf verschiedenen Systemen
erm�glicht.

%description -l fr
Ce package offre un client pour le 'Internet Talk Protocol', qui
permet la conversation un-a-un dans la discussion entre les
utilisateurs de diff�rents syst�mes.

%description -l pl
Pakiet ten zawiera klienta dla internetowego protoko�u talk, kt�ry
umo�liwia komunikacj� mi�dzy u�ytkownikami na r�nych systemach.

%description -l tr
Bu paket internet talk hizmeti i�in bir istemci ve sunucu
i�ermektedir. Bu program 'konu�mak' isteyen ki�ilerin terminalinde iki
b�l�m a�acakt�r. Kullan�c�lardan her biri kendi yazd�klar�n� ekran�n
alt k�sm�nda, kar�� taraf�n yazd�klar�n� ise �st k�s�mda
g�receklerdir.

%package -n ntalkd
Summary:	Talk daemon for one-on-one Internet chatting
Summary(de):	Talk-daemon f�r 1:1-Internet-Schw�tzchen
Summary(fr):	Daemon talk pour les conversations � deux sur l'Internet
Summary(pl):	Serwer talk do rozm�w jeden-na-jeden w Internecie
Summary(tr):	Internet �zerinde birebir konu�ma - talk - sistemi
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Requires:	inetdaemon
Prereq:		rc-inetd >= 0.8.1
Obsoletes:	talk-server

%description -n ntalkd
This package provides a daemon for the Internet talk protocol, which
allows one-on-one chatting between users on different systems.

%description -l de -n ntalkd
Dieses Paket enth�lt einen D�mon f�r das Internet-Talk- Protokoll, das
das Chatten von zwei Benutzern auf verschiedenen Systemen erm�glicht.

%description -l fr -n ntalkd
Ce package offre un d�mon pour le 'Internet Talk Protocol', qui permet
la conversation un-a-un dans la discussion entre les utilisateurs de
diff�rents syst�mes.

%description -l pl -n ntalkd
Pakiet ten zawiera serwe internetowego protoko�u talk, kt�ry umo�liwia
komunikacj� mi�dzy u�ytkownikami na r�nych systemach.

%description -l tr -n ntalkd
Bu paket internet talk hizmeti i�in bir istemci ve sunucu
i�ermektedir. Bu program 'konu�mak' isteyen ki�ilerin terminalinde iki
b�l�m a�acakt�r. Kullan�c�lardan her biri kendi yazd�klar�n� ekran�n
alt k�sm�nda, kar�� taraf�n yazd�klar�n� ise �st k�s�mda
g�receklerdir.

%prep
%setup -q -n netkit-ntalk-%{version}
%patch -p1

%build
./configure --with-c-compiler=gcc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,8}} \
	$RPM_BUILD_ROOT/etc/sysconfig/rc-inetd

%{__make} install INSTALLROOT=$RPM_BUILD_ROOT MANDIR=%{_mandir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ntalkd
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/talkd

gzip -9nf README BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%post -n ntalkd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet sever" 1>&2
fi

%postun -n ntalkd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/talk
%{_mandir}/man1/talk.1*

%files -n ntalkd
%defattr(644,root,root,755)
%doc README.gz BUGS.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%attr(640,root,root) %config(noreplace) %verify(not mtime md5 size) /etc/sysconfig/rc-inetd/*
