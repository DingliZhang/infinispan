Name:          infinispan
Version:       8.2.4
Release:       11
Summary:       Data grid platform
License:       ASL 2.0 and LGPLv2+ and Public Domain
URL:           http://infinispan.org/
Source0:       https://github.com/infinispan/infinispan/archive/8.2.4.Final/infinispan-8.2.4.Final.tar.gz

# Port to lucene 6.x
Patch0:        lucene-6.patch
Patch1:        implement-abstract-functions-extended-from-class-Directory.patch
Patch2:        CVE-2016-0750.patch
Patch3:        CVE-2017-15089-1.patch
Patch4:        CVE-2017-15089-2.patch

BuildRequires: maven-local mvn(com.clearspring.analytics:stream) mvn(com.mchange:c3p0)
BuildRequires: mvn(commons-logging:commons-logging) mvn(commons-pool:commons-pool)
BuildRequires: mvn(gnu-getopt:getopt) mvn(io.netty:netty-all) mvn(javax.enterprise:cdi-api)
BuildRequires: mvn(net.jcip:jcip-annotations) mvn(org.antlr:antlr-runtime)
BuildRequires: mvn(org.antlr:antlr3-maven-plugin) mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin) mvn(org.apache.geronimo.specs:geronimo-jcache_1.0_spec)
BuildRequires: mvn(org.apache.httpcomponents:httpclient) mvn(org.apache.logging.log4j:log4j-core)
BuildRequires: mvn(org.apache.logging.log4j:log4j-jcl) mvn(org.apache.logging.log4j:log4j-slf4j-impl)
BuildRequires: mvn(org.apache.lucene:lucene-core) >= 5.3.1 mvn(org.apache.lucene:lucene-analyzers-common) >= 5.3.1
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin) mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin) mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin) mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi) mvn(org.eclipse.osgi:org.eclipse.osgi.services)
BuildRequires: mvn(org.fusesource.leveldbjni:leveldbjni) mvn(org.hibernate:hibernate-core)
BuildRequires: mvn(org.hibernate.javax.persistence:hibernate-jpa-2.1-api)
BuildRequires: mvn(org.infinispan.protostream:protostream) >= 3.0.4 mvn(org.iq80.leveldb:leveldb)
BuildRequires: mvn(org.javassist:javassist) mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.aesh:aesh) mvn(org.jboss.arquillian:arquillian-bom:pom:)
BuildRequires: mvn(org.jboss.logging:jboss-logging) mvn(org.jboss.logging:jboss-logging-processor:1)
BuildRequires: mvn(org.jboss.marshalling:jboss-marshalling-osgi) mvn(org.jboss.maven.plugins:maven-injection-plugin)
BuildRequires: mvn(org.jboss.remotingjmx:remoting-jmx) mvn(org.jboss.sasl:jboss-sasl)
BuildRequires: mvn(org.jboss.shrinkwrap:shrinkwrap-bom:pom:)
BuildRequires: mvn(org.jboss.shrinkwrap.descriptors:shrinkwrap-descriptors-bom:pom:)
BuildRequires: mvn(org.jboss.shrinkwrap.resolver:shrinkwrap-resolver-bom:pom:)
BuildRequires: mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.1_spec)
BuildRequires: mvn(org.jboss.xnio:xnio-nio) mvn(org.jgroups:jgroups) >= 3.6.4
BuildRequires: mvn(org.kohsuke.metainf-services:metainf-services) mvn(org.scala-lang:scala-compiler)
BuildRequires: mvn(org.springframework:spring-context) mvn(org.wildfly.core:wildfly-controller)
BuildRequires: mvn(org.wildfly.core:wildfly-core-parent:pom:)

# Public Domain: ./commons/src/main/java/org/infinispan/commons/util/Base64.java
Provides:      bundled(java-base64) = 4.2

BuildArch:     noarch

%description
Infinispan is an extremely scalable, highly available data grid
platform - 100% open source, and written in Java. The purpose of
Infinispan is to expose a data structure that is highly concurrent,
designed ground-up to make the most of modern multi-processor/multi-core
architectures while at the same time providing distributed cache
capabilities.  At its core Infinispan exposes a Cache interface which
extends java.util.Map. It is also optionally is backed by a peer-to-peer
network architecture to distribute state efficiently around a data grid.

%package help
Summary:       Help for %{name}
Provides:      %{name}-javadoc = %{version}-%{release}
Obsoletes:     %{name}-javadoc < %{version}-%{release}

%description help
This package contains the help documentation for %{name}.

%prep
%autosetup -n %{name}-%{version}.Final -p1

find .  -name "*.jar" -or -name "*.class" | xargs rm -rf

# Rename the license file
cp -pr license/src/main/resources/META-INF/LICENSE.txt.vm LICENSE.txt

# Checkstyle is unnecessary for RPM builds
%pom_disable_module checkstyle
%pom_remove_plugin -r org.apache.maven.plugins:maven-checkstyle-plugin

%pom_disable_module all
%pom_disable_module all/cli
%pom_disable_module all/embedded
%pom_disable_module all/embedded-query
%pom_disable_module all/remote
%pom_disable_module as-modules/embedded
%pom_disable_module as-modules/client
%pom_disable_module demos/gui
%pom_disable_module demos/distexec
%pom_disable_module demos/lucene-directory-demo
%pom_disable_module demos/gridfs-webdav
%pom_disable_module demos/nearcache
%pom_disable_module demos/nearcache-client
%pom_disable_module integrationtests
%pom_disable_module integrationtests/as-integration-embedded
%pom_disable_module integrationtests/as-integration-client
%pom_disable_module integrationtests/as-lucene-directory
%pom_disable_module integrationtests/compatibility-mode-it
%pom_disable_module integrationtests/cdi-jcache-it
%pom_disable_module integrationtests/security-it
%pom_disable_module integrationtests/security-manager-it
%pom_disable_module integrationtests/osgi
%pom_disable_module integrationtests/cdi-weld-se-it
%pom_disable_module integrationtests/all-embedded-it
%pom_disable_module integrationtests/all-embedded-query-it
%pom_disable_module integrationtests/all-remote-it
%pom_disable_module javadoc
%pom_disable_module persistence/rest
%pom_disable_module rhq-plugin
%pom_disable_module server/integration
%pom_disable_module server/rest
%pom_disable_module tck-runner jcache

%pom_disable_module spring/spring4
%pom_disable_module spring/spring4/spring4-common
%pom_disable_module spring/spring4/spring4-embedded
%pom_disable_module spring/spring4/spring4-remote

%pom_xpath_set pom:properties/pom:version.jboss.logging.processor 1 parent

%pom_remove_plugin ":maven-remote-resources-plugin" parent
# org.scala-tools:maven-scala-plugin:2.15.2 used for generate-blueprint task
%pom_remove_plugin -r ":maven-scala-plugin" parent jcache/embedded

%pom_remove_plugin :jetty-maven-plugin persistence/rest

%pom_remove_plugin :maven-invoker-plugin jcache/embedded
%pom_remove_plugin :maven-failsafe-plugin parent

# Use eclipse apis: type ServiceTracker does not take parameters
%pom_change_dep -r org.osgi:org.osgi.core org.eclipse.osgi:org.eclipse.osgi commons persistence/jpa osgi bom
%pom_remove_dep -r org.osgi:org.osgi.compendium commons persistence/jpa
%pom_change_dep -r org.osgi:org.osgi.compendium org.eclipse.osgi:org.eclipse.osgi.services osgi bom

%pom_change_dep -r javax.cache:cache-api org.apache.geronimo.specs:geronimo-jcache_1.0_spec:1.0-alpha-1 jcache/commons jcache/embedded jcache/remote bom core cdi/remote

%pom_change_dep :leveldbjni-all :leveldbjni persistence/leveldb

# https://bugs.openjdk.java.net/browse/JDK-8067747
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration" '
<useIncrementalCompilation>false</useIncrementalCompilation>
<source>${version.java}</source>
<target>${version.java}</target>' commons
for p in core server/core persistence/jdbc lucene/lucene-directory \
 query server/hotrod \
 tree client/hotrod-client persistence/remote persistence/leveldb server/memcached \
 server/websocket cli/cli-interpreter cdi/embedded cdi/remote jcache/embedded;do
%pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin:3.0 ${p} '
<configuration>
 <useIncrementalCompilation>false</useIncrementalCompilation>
 <source>${version.java}</source>
 <target>${version.java}</target>
 <encoding>UTF-8</encoding>
</configuration>'
done

# Compile scala stuff
for p in core \
 hotrod \
 memcached;do
%pom_remove_plugin ":maven-scala-plugin" server/${p}
%pom_add_plugin org.apache.maven.plugins:maven-antrun-plugin:1.7 server/${p} '
<executions>
  <execution>
    <id>compile</id>
    <phase>process-sources</phase>
    <configuration>
      <tasks>
        <property name="build.compiler" value="extJavac"/>
        <taskdef resource="scala/tools/ant/antlib.xml" classpathref="maven.compile.classpath"/>
        <mkdir dir="target/classes"/>
        <scalac srcdir="src/main" destdir="target/classes" classpathref="maven.compile.classpath" encoding="UTF-8">
          <include name="**/*.*"/>
        </scalac>
      </tasks>
    </configuration>
      <goals>
        <goal>run</goal>
      </goals>
  </execution>
</executions>
<dependencies>
  <dependency>
      <groupId>org.scala-lang</groupId>
      <artifactId>scala-compiler</artifactId>
      <version>${version.scala}</version>
  </dependency>
</dependencies>'
done

%pom_disable_module lucene/directory-provider
%pom_disable_module object-filter
%pom_disable_module query
%pom_disable_module remote-query/remote-query-server
%pom_disable_module scripting
%pom_disable_module server/hotrod
%pom_disable_module tasks
%pom_disable_module tools

%pom_xpath_remove "pom:dependency[pom:artifactId = 'tools']/pom:scope" tools
%pom_xpath_remove "pom:dependency[pom:artifactId = 'tools']/pom:systemPath" tools

# org.hibernate:hibernate-search-engine:tests:5.5.1.Final
%pom_xpath_remove "pom:dependency[pom:groupId = 'org.hibernate']/pom:classifier" lucene/directory-provider

# This component is now owned and maintained by the Infinispan team
%mvn_alias :infinispan-directory-provider org.hibernate:hibernate-search-infinispan

%build

%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md README-i18n.md
%license LICENSE.txt

%files help -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Wed Nov 9 2022 liyanan <liyanan32@h-partners.com>  - 8.2.4-11
- Change source

* Fri Dec 24 2021 yaoxin <yaoxin30@huawei.com> - 8.2.4-10
- This package depends on log4j.After the log4j vulnerability CVE-2021-45105 is fixed,the version needs to be rebuild.

* Thu Dec 16 2021 wangkai <wangkai385@huawei.com> - 8.2.4-9
- This package depends on log4j.After the log4j vulnerability CVE-2021-44228 is fixed,the version needs to be rebuild.

* Thu Mar 4 2021 zhanghua<zhanghua40@huawei.com> - 8.2.4-8
- fix CVE-2016-0750 CVE-2017-15089

* Tue Mar 10 2020 xuxijian<xuxijian@huawei.com> - 8.2.4-7
- Package init
