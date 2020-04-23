from django.db import models

# Create your models here.
#标签
class Tag(models.Model):
    tagName = models.CharField('Tag', max_length=5)

    def __unicode__(self):
        return self.tagName

    def __str__(self):
        return '%s' % (self.tagName)


#文章
class Article(models.Model):
    title = models.CharField('Title', max_length=10)
    author = models.CharField('Author', max_length=16)
    pub_date = models.DateTimeField('Data Published', auto_now_add=True)
    content = models.TextField('Content', blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s' % (self.title, self.tag)


    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']



#评论
class Comments(models.Model):
    article = models.ForeignKey(Article, verbose_name='博客', on_delete=models.CASCADE)
    visterName = models.CharField('Name', max_length=16)
    email = models.EmailField('Email')
    content = models.CharField('Comment', max_length=240)
    pub_date = models.DateTimeField('Data Published', auto_now_add=True)

    def __unicode__(self):
        return self.content


    def __str__(self):
        return '%s, %s' % (self.visterName, self.content)