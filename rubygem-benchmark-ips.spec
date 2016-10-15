#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-benchmark-ips
Version  : 2.7.2
Release  : 15
URL      : https://rubygems.org/downloads/benchmark-ips-2.7.2.gem
Source0  : https://rubygems.org/downloads/benchmark-ips-2.7.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-hoe
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rdoc

%description
[![Gem Version](https://badge.fury.io/rb/benchmark-ips.svg)](http://badge.fury.io/rb/benchmark-ips)
[![Build Status](https://secure.travis-ci.org/evanphx/benchmark-ips.svg)](http://travis-ci.org/evanphx/benchmark-ips)
[![Inline docs](http://inch-ci.org/github/evanphx/benchmark-ips.svg)](http://inch-ci.org/github/evanphx/benchmark-ips)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n benchmark-ips-2.7.2
gem spec %{SOURCE0} -l --ruby > rubygem-benchmark-ips.gemspec

%build
export LANG=C
gem build rubygem-benchmark-ips.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
benchmark-ips-2.7.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/benchmark-ips-2.7.2
ruby -v -I.:lib:test test*/test_*.rb || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/benchmark-ips-2.7.2.gem
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/.autotest
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/Gemfile.lock
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/History.txt
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/Manifest.txt
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/README.md
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/lib/benchmark/compare.rb
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/lib/benchmark/ips.rb
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/lib/benchmark/ips/job.rb
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/lib/benchmark/ips/job/entry.rb
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/lib/benchmark/ips/job/stdout_report.rb
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/lib/benchmark/ips/report.rb
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/lib/benchmark/ips/share.rb
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/lib/benchmark/ips/stats/bootstrap.rb
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/lib/benchmark/ips/stats/sd.rb
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/lib/benchmark/timing.rb
/usr/lib64/ruby/gems/2.3.0/gems/benchmark-ips-2.7.2/test/test_benchmark_ips.rb
/usr/lib64/ruby/gems/2.3.0/specifications/benchmark-ips-2.7.2.gemspec
