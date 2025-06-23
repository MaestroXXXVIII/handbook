from dishka import Provider, Scope, provide

from src.features.organization.application.interactors import (
    GetOrganizationByIdInteractor,
    GetOrganizationByTitleInteractor,
    GetOrganizationsInteractor,
)


class OrganizationInteractorProvider(Provider):
    scope = Scope.REQUEST

    get_organizations = provide(GetOrganizationsInteractor)
    get_organization_by_id = provide(GetOrganizationByIdInteractor)
    get_organization_by_title = provide(GetOrganizationByTitleInteractor)
