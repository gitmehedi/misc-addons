{
    'name' : 'Signature templates for user emails',
    'version' : '1.0.0',
    'author' : 'Ivan Yelizariev',
    'category' : 'Sale',
    'website' : 'https://it-projects.info',
    'description': """
Allows create signature templates for users. For example,

    ---

    <p>${user.name}, ${user.function} of ${user.partner_id.company_id.name}</p>

    <p>${user.phone}, 

    % if user.mobile

    ${user.mobile}, 

    % endif

    ${user.email}</p>

Will be converted to 

    ---

    <p>Bob, sale manager of You Company</p>

    <p>+123456789, sales@example.com</p>

Tested on 8.0 ab7b5d7
    """,
    'depends' : ['base'],
    'data':[
        'res_users_signature_views.xml',
        'security/res_users_signature_security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True
}