# Generated by Django 3.2.17 on 2023-02-28 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newswebsite', '0002_auto_20230225_0033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章信息表'},
        ),
        migrations.AlterModelOptions(
            name='best',
            options={'verbose_name': '精选文章', 'verbose_name_plural': '精选文章信息表'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '新闻分类', 'verbose_name_plural': '新闻分类信息表'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '评论', 'verbose_name_plural': '评论信息表'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户信息表'},
        ),
        migrations.AlterField(
            model_name='best',
            name='select_reason',
            field=models.CharField(choices=[('今日热闻', '今日热闻'), ('首页推荐', '首页推荐'), ('小编推荐', '小编推荐')], max_length=50, verbose_name='推荐'),
        ),
    ]
