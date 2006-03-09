Summary:	Talk client for one-on-one Internet chatting
Summary(de):	Talk-client für 1:1-Internet-Schwätzchen
Summary(es):	Diálogo de cliente charlas uno a uno en internet
Summary(fr):	Client talk pour les conversations à deux sur l'Internet
Summary(pl):	Klient talk do rozmów jeden-na-jeden w Internecie
Summary(pt_BR):	Conversa de cliente para um-em-um para Internet
Summary(ru):	äÅÍÏÎ É ËÌÉÅÎÔ talk
Summary(tr):	Internet üzerinde birebir konuþma - talk - sistemi
Summary(uk):	äÅÍÏÎ ÔÁ ËÌ¦¤ÎÔ talk
Name:		ntalk
Version:	0.17
Release:	8
License:	BSD
Group:		Applications/Networking
Source0:	ftp://ftp.linux.org.uk/pub/linux/Networking/netkit/netkit-%{name}-%{version}.tar.gz
# Source0-md5:	e3c57208f8644ae206dab5e236daf7b3
Source1:	%{name}d.inetd
Source2:	talkd.inetd
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source3-md5:	730be3085782af4ff21151d9c106549d
Patch0:		netkit-%{name}-misc.patch
Patch1:		%{name}-include.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	inetutils-talk
Obsoletes:	talk
Obsoletes:	ntalk-client

%description
This package provides a client for the Internet talk protocol, which
allows one-on-one chatting between users on different systems.

%description -l de
Dieses Paket enthält einen Client für das Internet-Talk- Protokoll,
das das Chatten von zwei Benutzern auf verschiedenen Systemen
ermöglicht.

%description -l es
Diálogo de cliente charlas uno a uno en internet.

%description -l fr
Ce package offre un client pour le 'Internet Talk Protocol', qui
permet la conversation un-a-un dans la discussion entre les
utilisateurs de différents systèmes.

%description -l pl
Pakiet ten zawiera klienta dla internetowego protoko³u talk, który
umo¿liwia komunikacjê miêdzy u¿ytkownikami na ró¿nych systemach.

%description -l pt_BR
Este pacote fornece um cliente e um daemon para o protocolo talk, que
permite a conversa um-para-um entre usuários em diferentes sistemas.

%description -l ru
÷ ÜÔÏÍ ÐÁËÅÔÅ ÓÏÄÅÒÖÉÔÓÑ ËÌÉÅÎÔ É ÄÅÍÏÎ ÐÒÏÔÏËÏÌÁ Internet talk,
ËÏÔÏÒÙÊ ÐÏÚ×ÏÌÑÅÔ ÏÒÇÁÎÉÚÏ×ÁÔØ ÞÁÔ ÍÅÖÄÕ ÐÏÌØÚÏ×ÁÔÅÌÑÍÉ ÎÁ ÒÁÚÎÙÈ
ÓÉÓÔÅÍÁÈ.

%description -l tr
Bu paket internet talk hizmeti için bir istemci ve sunucu
içermektedir. Bu program 'konuþmak' isteyen kiþilerin terminalinde iki
bölüm açacaktýr. Kullanýcýlardan her biri kendi yazdýklarýný ekranýn
alt kýsmýnda, karþý tarafýn yazdýklarýný ise üst kýsýmda
göreceklerdir.

%description -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ËÌ¦¤ÎÔ ÔÁ ÄÅÍÏÎ ÐÒÏÔÏËÏÌÕ Internet talk, ÝÏ ÄÏÚ×ÏÌÑ¤
ÏÒÇÁÎ¦ÚÕ×ÁÔÉ ÞÁÔ Í¦Ö ËÏÒÉÓÔÕ×ÁÞÁÍÉ ÎÁ Ò¦ÚÎÉÈ ÓÉÓÔÅÍÁÈ.

%package -n ntalkd
Summary:	Talk daemon for one-on-one Internet chatting
Summary(de):	Talk-daemon für 1:1-Internet-Schwätzchen
Summary(es):	Servidor de diálogo charlas uno a uno en internet
Summary(fr):	Daemon talk pour les conversations à deux sur l'Internet
Summary(pl):	Serwer talk do rozmów jeden-na-jeden w Internecie
Summary(pt_BR):	Servidor de conversa um-em-um internet
Summary(tr):	Internet üzerinde birebir konuþma - talk - sistemi
Group:		Networking/Daemons
Requires:	inetdaemon
Prereq:		rc-inetd >= 0.8.1
Provides:	talkd
Obsoletes:	inetutils-talkd
Obsoletes:	talk-server

%description -n ntalkd
This package provides a daemon for the Internet talk protocol, which
allows one-on-one chatting between users on different systems.

%description -n ntalkd -l de
Dieses Paket enthält einen Dämon für das Internet-Talk- Protokoll, das
das Chatten von zwei Benutzern auf verschiedenen Systemen ermöglicht.

%description -n ntalkd -l es
Diálogo de servidor charlas uno a uno en internet.

%description -n ntalkd -l fr
Ce package offre un démon pour le 'Internet Talk Protocol', qui permet
la conversation un-a-un dans la discussion entre les utilisateurs de
différents systèmes.

%description -n ntalkd -l pl
Pakiet ten zawiera serwer internetowego protoko³u talk, który
umo¿liwia komunikacjê miêdzy u¿ytkownikami na ró¿nych systemach.

%description -n ntalkd -l pt_BR
Servidor talk.

%description -n ntalkd -l tr
Bu paket internet talk hizmeti için bir istemci ve sunucu
içermektedir. Bu program 'konuþmak' isteyen kiþilerin terminalinde iki
bölüm açacaktýr. Kullanýcýlardan her biri kendi yazdýklarýný ekranýn
alt kýsmýnda, karþý tarafýn yazdýklarýný ise üst kýsýmda
göreceklerdir.

%prep
%setup -q -n netkit-%{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
./configure \
	--with-c-compiler="%{__cc}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,8}} \
	$RPM_BUILD_ROOT/etc/sysconfig/rc-inetd

%{__make} install INSTALLROOT=$RPM_BUILD_ROOT MANDIR=%{_mandir}

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ntalkd
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/talkd
bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n ntalkd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
else
	echo "Type \"/etc/rc.d/init.d/rc-inetd start\" to start inet server" 1>&2
fi

%postun -n ntalkd
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload 1>&2
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/talk
%{_mandir}/man1/talk.1*
%lang(fi) %{_mandir}/fi/man1/talk.1*
%lang(fr) %{_mandir}/fr/man1/talk.1*
%lang(hu) %{_mandir}/hu/man1/talk.1*
%lang(it) %{_mandir}/it/man1/talk.1*
%lang(ja) %{_mandir}/ja/man1/talk.1*
%lang(pl) %{_mandir}/pl/man1/talk.1*

%files -n ntalkd
%defattr(644,root,root,755)
%doc README BUGS
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%lang(ja) %{_mandir}/ja/man8/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/*
