import React from 'react';
import {link} from 'react-router-dom'


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                <link to={'projects/${project.id}'}>{project.name}</link>
            </td>
            <td>
                <a href={project.repoUrl}>{project.repoUrl}</a>
            </td>
            <td>
                {project.createdAt}
            </td>
        </tr>
    )
}


const ProjectList = ({projects}) => {
    return (
        <div className="table-responsive">
            <table className="table table-striped table-sm">
                <thead>
                <tr>
                    <th>Project Name</th>
                    <th>Repo URL</th>
                    <th>Created at</th>
                </tr>
                </thead>
                <tbody>
                {projects?.map((project) => <ProjectItem key={project.id} project={project}/>)}
                </tbody>
            </table>
        </div>
    )
}

export default ProjectList