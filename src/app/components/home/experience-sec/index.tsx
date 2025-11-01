import React from 'react';

const ExperienceSec = () => {
    const experiences = [
        {
            year: "2024-Present",
            title: "Sr. Software Engr.",
            company: "Eplanet Globals",
            type: "Fulltime (onsite)",
            description: "MVC framework used for customized, data-driven web APIs for larger businesses and enterprises.Developing high-performance applications by writing testable, reusable, and efficient code. Documenting Node.js processes, including database schemas, as well as preparing reports."
        },
        {
            year: "2022-2024",
            title: "Backend Developer",
            company: "Cubix",
            type: "Fulltime (onsite)",
            description: "Designed and developed Restful APIs to maintain operations continuity and productivity. Developing and maintaining all server-side network components. Developed the concept of technical solutions based on customer needs to ensure satisfaction. Utilized SQL and NoSQL on the back-end component ensuring the operations of all deliverables while maintaining necessary technical knowledge and skills."
        },
        {
            year: "2020-2022",
            title: "Backend Developer",
            company: "CSquare Cosulting",
            type: "Fulltime (onsite)",
            description: "Capturing the best development practices & coding standards to decrease code complexity and improve maintainability of the shared libraries and components. Integrating with third-party services and external APIs. Maintaining newly developed and legacy web app. Performing unit & load testing for the critical progressive web application that helped to improve system's stability and scalability by identification critical performance issues during development phase."
        }
    ];

    return (
        <section>
            <div className="py-16 md:py-32">
                <div className="container mx-auto px-4">
                    <div className="flex items-center justify-between gap-2 border-b border-black pb-7 mb-9 md:mb-16">
                        <h2>Experience</h2>
                        <p className="text-xl text-primary">( 05 )</p>
                    </div>

                    <div className="space-y-7 md:space-y-12">
                        {experiences.map((exp, index) => (
                            <div key={index} className="grid grid-cols-1 sm:grid-cols-3 gap-2.5 md:gap-4 xl:gap-8 items-start relative">
                                <div className="">
                                    <h3 className="font-bold mb-2 text-black">{exp.year}</h3>
                                    <h4 className="text-lg font-normal">{exp.title}</h4>
                                </div>

                                <div className=" relative">
                                    {index < experiences.length && (
                                        <div className={`absolute left-0 top-3 w-px ${index < experiences.length - 1 ? 'h-40' : 'h-30'} bg-softGray`}></div>
                                    )}

                                    <div className="no-print absolute left-0 top-0 transform -translate-x-1/2">
                                        <div className={`no-print w-3.5 h-3.5 rounded-full border-1 bg-white flex items-center justify-center ${index === 0 ? 'border-primary' : 'border-black'
                                            }`}>
                                            {index === 0 && (
                                                <div className="w-1.5 h-1.5 rounded-full bg-primary"></div>
                                            )}
                                        </div>
                                    </div>

                                    <div className="pl-4 lg:pl-7">
                                        <div className="flex items-center gap-2 mb-1">
                                            <span className="text-xl text-black font-normal">{exp.company}</span>
                                        </div>
                                        <p className="text-base font-normal">{exp.type}</p>
                                    </div>
                                </div>

                                <div className="pl-8 sm:pl-0">
                                    <p className="leading-relaxed text-base">{exp.description}</p>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </section>
    );
};

export default ExperienceSec;