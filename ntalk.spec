Summary:	Talk client for one-on-one Internet chatting.
Summary(de):	Talk-client für 1:1-Internet-Schwätzchen.
Summary(fr):	Client talk pour les conversations à deux sur l'Internet.
Summary(pl):	Klient talk do rozmów jeden-na-jeden w Internecie.
Summary(tr):	Internet üzerinde birebir konuþma - talk - sistemi.
Name:		ntalk
Version:	0.11
Release:	1
Copyright:	BSD
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source:		ftp://sunsite.unc.edu/pub/Linux/system/network/chat/netkit-ntalk-%{version}.tar.gz
Patch0:		netkit-ntalk-misc.patch
Patch1:		netkit-ntalk-install.patch
Patch2:		netkit-ntalk-glibc21.patch
Requires:	inetd
BuildPrereq:	ncurses-devel
Obsoletes:	talk
Buildroot:	/tmp/%{name}-%{version}-root

%description
This package provides a daemon for the Internet talk protocol,
which allows one-on-one chatting between users on different systems.

%description -l de
Dieses Paket enthält einen Dämon für das Internet-Talk-
Protokoll, das das Chatten von zwei Benutzern auf verschiedenen
Systemen ermöglicht.

%description -l fr
Ce package offre un démon pour le 'Internet Talk Protocol',
qui permet la conversation un-a-un dans la discussion entre les
utilisateurs de différents systèmes.

%description -l pl
Pakiet ten zawiera demona dla internetowego protoko³u talk, 
który umo¿liwia	komunikacjê miêdzy u¿ytkownikami na ró¿nych systemach.

%description -l tr
Bu paket internet talk hizmeti için bir istemci ve sunucu içermektedir. Bu
program 'konuþmak' isteyen kiþilerin terminalinde iki bölüm açacaktýr.
Kullanýcýlardan her biri kendi yazdýklarýný ekranýn alt kýsmýnda, karþý
tarafýn yazdýklarýný ise üst kýsýmda göreceklerdir.

%package client
Summary:        Talk client for one-on-one Internet chatting.
Summary(de):    Talk-client für 1:1-Internet-Schwätzchen.
Summary(fr):    Client talk pour les conversations à deux sur l'Internet.
Summary(pl):    Klient talk do rozmów jeden-na-jeden w Internecie.
Summary(tr):    Internet üzerinde birebir konuþma - talk - sistemi.
Group:          Aplications/Networking
Group(pl):      Aplikacje/Sieciowe
Requires:	%{name}-%{version}

%description client
This package provides a client for the Internet talk protocol,
which allows one-on-one chatting between users on different systems.

%description -l de client
Dieses Paket enthält einen Client für das Internet-Talk-
Protokoll, das das Chatten von zwei Benutzern auf verschiedenen
Systemen ermöglicht.

%description -l fr client
Ce package offre un client pour le 'Internet Talk Protocol',
qui permet la conversation un-a-un dans la discussion entre les
utilisateurs de différents systèmes.

%description -l pl client
Pakiet ten zawiera klienta dla internetowego protoko³u talk,
który umo¿liwia komunikacjê miêdzy u¿ytkownikami na ró¿nych systemach.

%description -l tr client
Bu paket internet talk hizmeti için bir istemci ve sunucu içermektedir. Bu
program 'konuþmak' isteyen kiþilerin terminalinde iki bölüm açacaktýr.
Kullanýcýlardan her biri kendi yazdýklarýný ekranýn alt kýsmýnda, karþý
tarafýn yazdýklarýný ise üst kýsýmda göreceklerdir.

%prep
%setup -q -n netkit-ntalk-0.11
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS -w -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{bin,sbin,man/{man1,man8}}

make INSTALLROOT=$RPM_BUILD_ROOT install

gzip -9nf $RPM_BUILD_ROOT/usr/man/man[18]/* \
	README BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz BUGS.gz

%attr(711,root,root) /usr/sbin/*
/usr/man/man8/*

%files client
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/talk
/usr/man/man1/talk.1.gz

%changelog
* Mon Apr 19 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.11-1]
- added "BuildPrereq: ncurses-devel".

* Fri Apr 16 1999 Piotr Czerwiñski <pius@pld.org.pl>
- updated to 0.11,
- added ntalk-client subpackage,
- added Obsoletes: talk,
- added netkit-ntalk-glibc21.patch,
- simplifications in %install (added netkit-ntalk-install.patch),
- fixed Group description and added Group(pl),
- fixed Summary and Summary(pl),
- changed Buildroot to /tmp/%{name}-%{version}-root,
- removed man group from man pages,
- added gzipping documentation and man pages,
- changes in %files,
- cosmetic changes for common l&f.

* Sat Aug 01 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.10-4d]
- build against glibc-2.1,
- removed talk client,
- renamed daemons to talkd and ntalkd,
- added pl translation,
- added build-root support,
- moved %changelog at the end of spec,
- added %doc,
- restricted ELF binary permission.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 14 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
