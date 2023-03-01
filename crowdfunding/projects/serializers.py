from rest_framework import serializers

from .models import Comment, Pledge, Project

# for every model, create a serializer.
# You can use a model serializer - like a model form.
# Can build itself off a model. Automates


class PledgeSerializer(serializers.ModelSerializer):
    """
    SlugRelatedField:
    changing the way project title displays in GET request. Displays the title of the project and not the id # using slug (human readable label)

    """

    project = serializers.SlugRelatedField(queryset=Project.objects.all(), slug_field="title")
    supporter = serializers.SerializerMethodField()
    supporter_avatar = serializers.SerializerMethodField()

    class Meta:
        model = Pledge
        fields = ["id", "amount", "comment", "anonymous", "project", "supporter","supporter_avatar","date_pledged"]
        read_only_fields = [
            "id",
            "supporter",
        ]  # added to remove the needs to input a supporter {automates to logged in user}

    def get_supporter(self, instance):
        """

        if the instance (supporter) has anonymous = True:
            replace True with "anonymous"
        else
            replace False with the username of the supporter
        """
        if instance.anonymous:
            return "anonymous"
        else:
            return instance.supporter.username

    def get_supporter_avatar(self, instance):
        # providing access to the the avatar of the supporter
        return instance.supporter.avatar


class PledgeDetailSerializer(PledgeSerializer):
    """
    Slug:changing the way project title displays in POST or PUT request. Displays the title of the project and not the id # using slug (human readable label)
    """

    project = serializers.SlugRelatedField(queryset=Project.objects.all(), slug_field="title")

    class Meta:
        model = Pledge
        fields = [
            "id",
            "amount",
            "comment",
            "anonymous",
            "project",
            "supporter",
            "supporter_avatar",
            "date_pledged"]
        read_only_fields = ["id", "supporter", "amount", "project"]


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner_id")
    sum_pledges = serializers.ReadOnlyField()
    goal_balance = serializers.ReadOnlyField()
    funding_status = serializers.ReadOnlyField()
    owner = serializers.SerializerMethodField()
    owner_avatar = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "goal",
            "image",
            "is_open",
            "date_created",
            "deadline",
            "owner",
            "sum_pledges",
            "goal_balance",
            "funding_status",
            "owner_avatar"
        ]
        read_only_fields = ["id", "owner", "sum_pledges", "goal_balance", "funding_status"]

    def get_owner(self, instance):
        return instance.owner.username

    def get_owner_avatar(self, instance):
        # providing access to the the avatar of the owner
        return instance.owner.avatar


class CommentSerializer(serializers.ModelSerializer):
    project = serializers.SlugRelatedField(queryset=Project.objects.all(), slug_field="title")
    commenter = serializers.ReadOnlyField(source="commenter.username")
    commenter_avatar = serializers.SerializerMethodField()


    class Meta:
        model = Comment
        fields = ["id", "created", "body", "commenter", "project","commenter_avatar"]
        read_only_fields = [
            "id",
            "commenter",
        ]
    # added to remove the needs to input a supporter {automates to logged in user}

    def get_commenter_avatar(self, instance):
        # providing access to the the avatar of the commenter
        return instance.commenter.avatar


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "goal",
            "image",
            "is_open",
            "date_created",
            "deadline",
            "owner",
            "owner_avatar",
            "sum_pledges",
            "goal_balance",
            "funding_status",
            "pledges",
            "comments",
        ]
        read_only_fields = ["id", "owner", "sum_pledges", "goal_balance", "funding_status"]

    # split out from Project Serializer to reduce amount of data fetching when viewing all projects
    # put it in views
