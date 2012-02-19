%global packname  networksis
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.4
Release:          1
Summary:          Simulate bipartite graphs with fixed marginals through sequential importance sampling
Group:            Sciences/Mathematics
License:          GPL-3 + file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-ergm R-network 
Requires:         R-snow 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-ergm R-network
BuildRequires:    R-snow 

%description
Tools to simulate bipartite networks/graphs with the degrees of the nodes
fixed and specified. Part of the "statnet" suite of packages for network

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
