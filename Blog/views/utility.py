from ..models.post import BasePost, Post, User


class FakePost(BasePost):    
    def __init__(self, title, first_writer,
                other_writers, first_paragraph,
                post_content):
        self._title = title
        self._first_writer = first_writer
        self._other_writers  = other_writers
        self._first_paragraph = first_paragraph
        self._post_content=post_content

    @property
    def title(self):
        return self._title
    @property
    def first_writer(self):
        return self._first_writer
    @property
    def other_writers(self):
        return self._other_writers
    @property
    def first_paragraph(self):
        return self._first_paragraph
    @property
    def post_content(self):
        return self._post_content

    def __repr__(self):
        return '<FakePost {}>'.format(self.title)
    
def get_posts(writername=None):
    if writername is None:
        return Post.query.all()
    else:
        writer = User.query.filter_by(username=writername).first()
        writer_post_relationships = writer.posts
        _post_first_writer = []
        _post_other_writer = []
        for writer_post in writer_post_relationships:
            if writer_post.is_first_author:
                _post_first_writer.append(writer_post.post)
            else:
                _post_other_writer.append(writer_post.post)
        posts = _post_first_writer.extend(_post_other_writer)
        return posts


post_titles = ['First', 'Second', 'Third', 'Fouth', 'Fifth',
                    'Sixth', 'Seventh', 'Eight', 'Nineth', 'Tenth']
post_writers = ['micheal', 'kfl', 'lrq', 'zl', 'zyq',
                        'ny', 'lzj', 'xzr', 'zs', 'ls']
first_paragraph = '''###About the responsive mobilt-first
We build responsive, mobile-first projects on the web with the world's most popular front-end component library.Bootstrap is an open source toolkit for developing with HTML, CSS, and JS. Quickly prototype your ideas or build your entire app with our Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful plugins built on jQuery.
'''

post_content ='''
# 支撑起整个互联网时代的 7 款开源软件

[TOCM]



开源软件现在成为整个互联网时代的支撑技术，你可能已经无法离开由开源软件构建起来的网络世界了。下面我们就来看看一些最重要的开源技术。

### 为互联网而生的操作系统linux

Linux是一款免费的操作系统，诞生于1991年，用户可以通过网络或其他途径免费获得，并可以任意修改其源代码。

#### linux A

它能运行主要的UNIX工具软件、应用程序和网络协议。它支持32位和64位硬件。Linux继承了Unix以网络为核心的设计思想，是一个性能稳 定的多用户网络操作系统。这个系统是由全世界各地的成千上万的程序员设计和实现的。其目的是建立不受任何商品化软件的版权制约的、全世界都能自由使用的 Unix兼容产品。

#### Test link heading [linux B](https://github.com/pandao/editor.md)  Test link heading

#### Test link heading [linux B](https://github.com/pandao/editor.md)   Test link heading [linux B](https://github.com/pandao/editor.md)  Test link heading, Test link heading, [linux B](https://github.com/pandao/editor.md)  Test link heading

##### linux B-1

###### linux B-1-1

###### linux B-1-2

##### linux B-2

###### linux B-2-1

###### linux B-2-2

#支撑起整个互联网时代的 7 款开源软件-2

Linux可以说是已经无处不在，像Android手机就是以Linux为基础开发的，世界上大多的超级计算机也都采用的Linux系统，大多数的 数据中心使用Linux作为其支撑操作系统。谷歌、百度、淘宝等都通过Linuxt提供了我们每天用的互联网服务。Linux在航空控制系统中也扮演着重 要角色。

###加密互联网的安全协议OpenSSL

OpenSSL是套开放源代码的软件库包，实现了SSL与TLS协议。OpenSSL可以说是一个基于密码学的安全开发包，囊括了主要的密码算法、常用的密钥和证书封装管理功能以及SSL协议，并提供了丰富的应用程序供测试或其它目的使用。

也可以说OpenSSL是网络通信提供安全及数据完整性的一种安全协议，SSL可以在Internet上提供秘密性传输，能使用户/服务器应用之间的通信不被攻击者窃听。OpenSSL被网银、在线支付、电商网站、门户网站、电子邮件等重要网站广泛使用。

去年OpenSSL爆出安全漏洞，因为其应用如此之广，该漏洞爆出让整个互联网都为之震颤。

### 互联网的记忆——MySQL

MySQL是一个开源的小型的数据库管理系统，原开发者为瑞典的MySQL AB公司，该公司于2008年被Sun公司收购。2009年，甲骨文公司（Oracle）收购Sun公司，MySQL成为Oracle旗下产品。

很多信息都是存在数据库里面的，很多工程师在开发一些的小型项目时都会采用这个MySQL数据库。MySQL为C、C++、JAVA、PHP等多重 编程语言提供了API接口。而且支持windows、Mac、Linux等多种系统。这种广泛的支持使其得到更多开发者的青睐，MySQL是开发者需要掌 握的数据库之一。

Mysql最初为小型应用而开发，但现在的Mysql已经不是一个小型数据库了。基本上所有的互联网公司都会使用这个数据库系统，一些金融交易也会 采用Mysql作为数据库引擎。Mysql通过相应的调优既可以支撑大规模的访问，又可以保证数据安全性，已经成为威胁传统商业数据库系统的重要力量。

### 万能开发工具Eclipse

Eclipse 是一个开放源代码的、基于Java的可扩展开发平台。Eclipse最初由OTI和IBM两家公司的IDE产品开发组创建，起始于1999年4月。目前由 IBM牵头，围绕着Eclipse项目已经发展成为了一个庞大的Eclipse联盟，有150多家软件公司参与到Eclipse项目中，其中包括 Borland、Rational Software、Red Hat及Sybase等。

就其本身而言，它只是一个框架和一组服务，用于通过插件组件构建开发环境。很多Java编程软件都是在Eclipse平台开发的，还有包括 Oracle在内的许多大公司也纷纷加入了该项目，并宣称Eclipse将来能成为可进行任何语言开发的IDE集大成者，使用者只需下载各种语言的插件即 可。

Eclipse并不是一个直接服务于消费者的产品，它更像一个工匠手中万用工具，用Eclipse开发者可以打造出各种充满创造性的服务来满足最终用户的需求。

### 互联网的门卫Apache

Apache HTTP Server（简称Apache）是Apache软件基金会的一个开放源码的网页服务器，可以在大多数计算机操作系统中运行，由于其多平台和安全性被广泛 使用，也是最流行的Web服务器端软件之一，市场占有率达60%左右。它快速、可靠并且可通过简单的API扩展，它可以和各种解释器配合使用，包括 PHP/Perl/Python等。

Apache就像一个负责的门卫，管理着服务器数据的进出。每当你在你的地址栏里输入 http://XXX.com 的时候，在遥远的远端，很有可能正是一台跑着Apache的服务器，将你需要的信息传输给浏览器。

###大数据的心脏Hadoop

Hadoop 是一个能够对大量数据进行分布式处理的软件框架，由Apache基金会开发。用户可以在不了解分布式底层细节的情况下，开发分布式程序。Hadoop 一 直帮助解决各种问题，包括超大型数据集的排序和大文件的搜索。它还是各种搜索引擎的核心，比如 Amazon 的 A9 和用于查找酒信息 的 Able Grape 垂直搜索引擎。阿里巴巴集团在商品推荐、用户行为分析、信用计算领域也都有hadoop的应用。

在“大数据”已经成为潮流的当下，Hadoop已经成为最主要的一项技术。可以毫不夸张的说，没有Hadoop，就没有大多数的大数据应用。可以说对一个不知道Hadoop的程序员而言，你已经out了。


#### Test link heading [linux B](https://github.com/pandao/editor.md)  Test link heading

#### Test link heading [linux B](https://github.com/pandao/editor.md)   Test link heading [linux B](https://github.com/pandao/editor.md)  Test link heading, Test link heading, [linux B](https://github.com/pandao/editor.md)  Test link heading

##### linux B-1

###### linux B-1-1

###### linux B-1-2

##### linux B-2

###### linux B-2-1

###### linux B-2-2

### 互联网的“排版引擎”WebKit

说是浏览器内核，其实“排版引擎”更容易理解一些。通过服务器传输给浏览器的信息只是一串乱糟糟的文本。要看到我们平时看到精美的网友，需要浏览器内核对这些文本进行解析，将枯燥的描述“画”成美丽的浏览界面。

WebKit 是一个开源的浏览器引擎，与之相应的引擎有 Gecko（Mozilla Firefox 等使用的排版引擎）和 Trident（也称为 MSHTML，IE 使用的排版引擎）。根据 StatCounter 的浏览器市场份额调查，于2012年11月，Webkit 市占超过了 40%，它已经成为拥有最大市场份额的 排版引擎，超越了 Internet Explorer 所使用的Trident 及 Firefox 所使用的 Gecko 引擎，并且 WebKit 份额正在逐年增加。

目前几乎所有网站和网银已经逐渐支持 WebKit 。WebKit 内核在手机上的应用也十分广泛，例如苹果的 Safari 、谷歌的 Chrome 浏览器都是基于这个框架来开发的。

### 小结

很多人可能尚未意识到，我们使用的电脑中运行有开源软件，手机中运行有开源软件，家里的电视也运行有开源软件，甚至小小的数码产品中也运行有开源软件，尤其是互联网服务器端软件，几乎全部是开源软件。毫不夸张地说，开源软件已经渗透到了我们日常生活的方方面面。

稿源：[钛媒体](http://www.tmtpost.com/194306.html)
$$x=\\frac{-b\pm\\sqrt{b^2-4ac}}{2a}$$

'''

def get_fake_posts(writer=None):
    fake_posts = []
    _index = 0
    if writer is not None:
        _index = post_writers.index(writer)
    for i in range(_index ,10):
        _post = FakePost(post_titles[i] + "Post", 
                        first_writer=post_writers[i],
                        other_writers=post_writers[i+1:],
                        first_paragraph=first_paragraph,
                        post_content=post_content)
        fake_posts.append(_post)
    return fake_posts
    
def get_fake_post(post_title):
    _index = post_titles.index(post_title.split("P")[0])
    return FakePost(post_titles[_index] + "Post",
                    first_writer=post_writers[_index],
                    other_writers=post_writers[_index + 1:],
                    first_paragraph=first_paragraph,
                    post_content=post_content)

x = '''
###About the responsive mobilt-first
We build responsive, mobile-first projects on the web with the world's most popular front-end component library.Bootstrap is an open source toolkit for developing with HTML, CSS, and JS. Quickly prototype your ideas or build your entire app with our Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful plugins built on jQuery.
'''    
