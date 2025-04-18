from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name
 
class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='news_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='news')
    tags = models.ManyToManyField(Tag, related_name='news')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Likes(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('news', 'user')
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
    def __str__(self):
        return f"{self.user.username} liked {self.news.title}"
    
    
    @property
    def like_count(self):
        return self.likes.count()


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.news.title}"
    
# class CommentLike(models.Model):
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_likes')
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='comment_likes')
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('comment', 'user')
#         verbose_name = 'Comment Like'
#         verbose_name_plural = 'Comment Likes'
#     def __str__(self):
#         return f"{self.user.username} liked {self.comment.content}"
#     @property
#     def comment_like_count(self):
#         return self.comment_likes.count()
