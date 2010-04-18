Summary:	commons-validator - framework to define validators
Summary(pl.UTF-8):	commons-validator - szkielet do definiowania metod kontrolujących poprawność
Name:		java-commons-validator
Version:	1.2.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/commons/validator/source/commons-validator-%{version}-src.tar.gz
# Source0-md5:	984074a3707c4a366f0b08db88d41e4d
URL:		http://commons.apache.org/validator/
BuildRequires:	ant >= 1.5
BuildRequires:	java-commons-beanutils
BuildRequires:	java-commons-collections
BuildRequires:	java-commons-digester
BuildRequires:	java-commons-logging
BuildRequires:	java-oro
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	java-commons-digester
Requires:	java-oro
Obsoletes:	jakarta-commons-validator
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The commons-validator package provides a simple, extendable framework
to define validators (validation methods) and validation rules in an
XML file. There is support for internationalization of validation
rules and error messages.

%description -l pl.UTF-8
Pakiet commons-validator udostępnia prosty, rozszerzalny szkielet do
definiowania "validatorów" (metod kontrolujących poprawność danych),
oraz reguł określających poprawność w pliku XML. Pakiet obsługuje
zlokalizowane reguły poprawności oraz komunikaty błędów.

%package javadoc
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja online do %{name}.

%prep
%setup -q -n commons-validator-%{version}

%build
required_jars="commons-beanutils-core commons-collections commons-digester commons-logging oro"
export CLASSPATH=$(%{_bindir}/build-classpath $required_jars)
%ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
for a in dist/*.jar; do
	jar=${a##*/}
	cp -a dist/$jar $RPM_BUILD_ROOT%{_javadir}/${jar%%.jar}-%{version}.jar
	ln -s ${jar%%.jar}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/$jar
done

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
	rm -f %{_javadocdir}/%{name}
fi

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
