/* tslint:disable */
/* eslint-disable */
/**
 * PrismAgent OpenAPI specification
 * OpenAPI specification for Decentralized Identifiers (DID) Operations
 *
 * The version of the OpenAPI document: 0.1.0
 * Contact: atala-coredid@iohk.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface VerificationCredentialSchemaInput
 */
export interface VerificationCredentialSchemaInput {
    /**
     * 
     * @type {string}
     * @memberof VerificationCredentialSchemaInput
     */
    id?: string;
    /**
     * 
     * @type {string}
     * @memberof VerificationCredentialSchemaInput
     */
    name: string;
    /**
     * 
     * @type {string}
     * @memberof VerificationCredentialSchemaInput
     */
    version: string;
    /**
     * 
     * @type {string}
     * @memberof VerificationCredentialSchemaInput
     */
    description?: string;
    /**
     * 
     * @type {Array<string>}
     * @memberof VerificationCredentialSchemaInput
     */
    attributes?: Array<string>;
    /**
     * 
     * @type {Date}
     * @memberof VerificationCredentialSchemaInput
     */
    authored?: Date;
    /**
     * 
     * @type {Array<string>}
     * @memberof VerificationCredentialSchemaInput
     */
    tags?: Array<string>;
}

/**
 * Check if a given object implements the VerificationCredentialSchemaInput interface.
 */
export function instanceOfVerificationCredentialSchemaInput(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "name" in value;
    isInstance = isInstance && "version" in value;

    return isInstance;
}

export function VerificationCredentialSchemaInputFromJSON(json: any): VerificationCredentialSchemaInput {
    return VerificationCredentialSchemaInputFromJSONTyped(json, false);
}

export function VerificationCredentialSchemaInputFromJSONTyped(json: any, ignoreDiscriminator: boolean): VerificationCredentialSchemaInput {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': !exists(json, 'id') ? undefined : json['id'],
        'name': json['name'],
        'version': json['version'],
        'description': !exists(json, 'description') ? undefined : json['description'],
        'attributes': !exists(json, 'attributes') ? undefined : json['attributes'],
        'authored': !exists(json, 'authored') ? undefined : (new Date(json['authored'])),
        'tags': !exists(json, 'tags') ? undefined : json['tags'],
    };
}

export function VerificationCredentialSchemaInputToJSON(value?: VerificationCredentialSchemaInput | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
        'name': value.name,
        'version': value.version,
        'description': value.description,
        'attributes': value.attributes,
        'authored': value.authored === undefined ? undefined : (value.authored.toISOString()),
        'tags': value.tags,
    };
}

