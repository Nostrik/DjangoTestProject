from django.contrib import admin
from app_library.models import Publisher, Autor, Book


class BookInline(admin.StackedInline):
	model = Book


class PublisherAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'city']
	list_filter = ['is_active', 'city']
	inlines = [BookInline]


class AutorAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name']
	search_fields = ['first_name', 'last_name', 'boigraphy']
	fieldsets = (
		('Основные сведения', {
			'fields': ('first_name', 'second_name', 'last_name', 'country', 'city')
			}),
		('Биографичесские данные', {
			'fields': ('univercity', 'birth_date', 'boigraphy'),
			'description': 'Различные данные из биографии автора',
			'classes': ['collapse']
			}),
		('Контакты', {
			'fields': ('email', 'phone', 'personal_page', 'facebook', 'twitter'),
			'description': 'Различные способы связи'
			})
		)


class BookAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'status']
	actions = ['mark_as_published', 'mark_as_draft', 'mark_as_review']

	def mark_as_published(self, request, queryset):
		queryset.update(status='p')

	def mark_as_draft(self, request, queryset):
		queryset.update(status='d')

	def mark_as_review(self, request, queryset):
		queryset.update(status='r')


	mark_as_published.short_description = 'Перевести в статус Опубликовано'
	mark_as_draft.short_description = 'Перевести в статус Черновик'
	mark_as_review.short_description = 'Перевести в статус Ревью'


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Book, BookAdmin)
